from app.db.questions.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.question import Question


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Question) -> Question:
        with self.cur() as cur:
            cur.execute(
                """
                INSERT INTO questions (category_id, question, answer)
                VALUES (%s, %s, %s)
                RETURNING id, category_id, question, answer;
                """,
                (msg.category_id, msg.question, msg.answer),
            )
            row = cur.fetchone()
            return Question(
                id=row[0],
                category_id=row[1],
                question=row[2],
                answer=row[3],
            )

    def get(self, req: SelectInput) -> list[Question]:
        with self.cur() as cur:
            sql = """
                SELECT id, category_id, question, answer
                FROM questions
            """
            params: list = []
            clauses: list = []

            if req.category_id:
                clauses.append("category_id = %s")
                params.append(req.category_id)

            if req.search:
                clauses.append("question ILIKE %s")
                params.append(f"%{req.search}%")

            if clauses:
                sql += " WHERE " + " AND ".join(clauses)

            sql += " ORDER BY question LIMIT %s OFFSET %s;"
            params.extend([req.limit, req.offset])

            cur.execute(sql, tuple(params))
            rows = cur.fetchall()

            return [
                Question(
                    id=r[0],
                    category_id=r[1],
                    question=r[2],
                    answer=r[3],
                )
                for r in rows
            ]
