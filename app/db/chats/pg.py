from app.db.chats.usecases import Interface, SelectInput, UpdateInput
from app.db.connector import get_cursor
from app.model.chat import Chat


class Repo(Interface):
    def __init__(self):
        # контекстный менеджер для курсора и коммита
        self.cur = get_cursor

    def create(self, msg: Chat) -> Chat:
        with self.cur() as cur:
            cur.execute(
                """
                INSERT INTO chats (user_id, status)
                VALUES (%s, %s)
                RETURNING
                  id,
                  user_id,
                  status,
                  EXTRACT(EPOCH FROM started_at)::BIGINT,
                  EXTRACT(EPOCH FROM COALESCE(closed_at, to_timestamp(0)))::BIGINT;
                """,
                (msg.user_id, msg.status),
            )
            row = cur.fetchone()
            return Chat(
                id=row[0],
                user_id=row[1],
                status=row[2],
                started_at=row[3],
                closed_at=row[4],
            )

    def get(self, req: SelectInput) -> list[Chat]:
        with self.cur() as cur:
            cur.execute(
                """
                SELECT
                  id,
                  user_id,
                  status,
                  EXTRACT(EPOCH FROM started_at)::BIGINT,
                  EXTRACT(EPOCH FROM COALESCE(closed_at, to_timestamp(0)))::BIGINT
                FROM chats
                ORDER BY started_at
                LIMIT %s OFFSET %s;
                """,
                (req.limit, req.offset),
            )
            rows = cur.fetchall()
            return [
                Chat(
                    id=r[0],
                    user_id=r[1],
                    status=r[2],
                    started_at=r[3],
                    closed_at=r[4],
                )
                for r in rows
            ]

    def update(self, chat: UpdateInput) -> Chat:
        with self.cur() as cur:
            if chat.status == "closed":
                cur.execute(
                    """
                    UPDATE chats
                    SET status    = %s,
                        closed_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                    RETURNING
                      id,
                      user_id,
                      status,
                      EXTRACT(EPOCH FROM started_at)::BIGINT,
                      EXTRACT(EPOCH FROM COALESCE(closed_at, to_timestamp(0)))::BIGINT;
                    """,
                    (chat.status, chat.id),
                )
            else:
                cur.execute(
                    """
                    UPDATE chats
                    SET status = %s
                    WHERE id = %s
                    RETURNING
                      id,
                      user_id,
                      status,
                      EXTRACT(EPOCH FROM started_at)::BIGINT,
                      EXTRACT(EPOCH FROM COALESCE(closed_at, to_timestamp(0)))::BIGINT;
                    """,
                    (chat.status, chat.id),
                )
            row = cur.fetchone()
            return Chat(
                id=row[0],
                user_id=row[1],
                status=row[2],
                started_at=row[3],
                closed_at=row[4],
            )
