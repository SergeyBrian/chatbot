from app.db.messages.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.message import Message


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor()

    def create(self, msg: Message) -> Message:
        with self.cur as cur:
            cur.execute(
                """
                INSERT INTO messages (dialog_id, sender, content)
                VALUES (%s, %s, %s)
                RETURNING id, EXTRACT(EPOCH FROM created_at)::BIGINT;
                """,
                (msg.dialog_id, msg.sender, msg.content),
            )
            msg_id, created_at_epoch = cur.fetchone()
            msg.id = msg_id
            msg.created_at = created_at_epoch
        return msg

    def get(self, req: SelectInput) -> List[Message]:
        with self.cur as cur:
            cur.execute(
                """
                SELECT id, dialog_id, sender, content,
                       EXTRACT(EPOCH FROM created_at)::BIGINT
                FROM messages
                WHERE dialog_id = %s
                ORDER BY created_at
                LIMIT %s OFFSET %s;
                """,
                (req.chat_id, req.limit, req.offset),
            )
            rows = cur.fetchall()
            return [
                Message(
                    id=r[0],
                    dialog_id=r[1],
                    sender=r[2],
                    content=r[3],
                    created_at=r[4],
                )
                for r in rows
            ]
