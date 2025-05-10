from app.db.messages.usecases import Interface, SelectInput, UpdateInput
from app.db.connector import get_cursor
from app.model.message import Message


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Message) -> Message:
        with self.cur() as cur:
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

    def get(self, req: SelectInput) -> list[Message]:
        with self.cur() as cur:
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

    def update(self, req: UpdateInput) -> Message:
        fields = []
        values = []
        if req.useful is not None:
            fields.append("useful = %s")
            values.append(req.useful)

        if not fields:
            raise ValueError("No fields to update")

        values.append(req.id)

        query = f"""
        UPDATE messages
        SET {', '.join(fields)}
        WHERE id = %s
        RETURNING id, dialog_id, sender, content, EXTRACT(EPOCH FROM created_at)::BIGINT, useful;
        """

        with self.cur() as cur:
            cur.execute(query, values)
            row = cur.fetchone()
            if not row:
                raise ValueError(f"Message with id {req.id} not found")
            return Message(
                id=row[0],
                dialog_id=row[1],
                sender=row[2],
                content=row[3],
                created_at=row[4],
                useful=row[5],
            )
