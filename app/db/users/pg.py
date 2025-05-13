from app.db.users.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.user import User


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: User) -> User:
        with self.cur() as cur:
            cur.execute(
                """
                INSERT INTO users (session_id, username)
                VALUES (%s, %s)
                RETURNING
                  id,
                  session_id,
                  username,
                  EXTRACT(EPOCH FROM created_at)::BIGINT;
                """,
                (msg.session_id, msg.name),
            )
            row = cur.fetchone()
            return User(
                id=row[0],
                session_id=row[1],
                name=row[2],
                created_at=row[3],
            )

    def get(self, req: SelectInput) -> User:
        with self.cur() as cur:
            if req.username:
                cur.execute(
                    """
                    SELECT
                      id,
                      session_id,
                      username,
                      EXTRACT(EPOCH FROM created_at)::BIGINT
                    FROM users
                    WHERE username = %s;
                    """,
                    (req.username,),
                )
            else:
                cur.execute(
                    """
                    SELECT
                      id,
                      session_id,
                      username,
                      EXTRACT(EPOCH FROM created_at)::BIGINT
                    FROM users
                    WHERE id = %s;
                    """,
                    (req.user_id,),
                )

            row = cur.fetchone()
            if not row:
                raise ValueError(
                    f"User not found by "
                    f"{'id='+str(req.user_id) if req.user_id else 'username='+req.username}"
                )

            return User(
                id=row[0],
                session_id=row[1],
                name=row[2],
                created_at=row[3],
            )
