from app.db.questions.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.question import Question
from app.model.question_csv import QuestionCSV


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Question) -> Question:
        with self.cur() as cur:
            cur.execute(
                """
                INSERT INTO knowledge_base (category, question, answer)
                VALUES (%s, %s, %s)
                RETURNING id, category, question, answer;
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
                SELECT id, category, question, answer
                FROM knowledge_base
            """
            params: list = []
            clauses: list = []

            if req.category_id:
                clauses.append("category = %s")
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

    def delete(self, id: int) -> int:
        with self.cur() as cur:
            sql = """
                DELETE FROM knowledge_base WHERE id = $1
            """
            params: list = [id]
            cur.execute(sql, tuple(params))

        return id

    def get_all_for_export(self) -> list[QuestionCSV]:
        with self.cur() as cur:
            cur.execute("""
                SELECT c.name, k.question, k.answer
                FROM knowledge_base k
                JOIN categories c ON k.category = c.id
            """)
            rows = cur.fetchall()
            from app.model.question_csv import QuestionCSV
            return [
                QuestionCSV(category=r[0], question=r[1], answer=r[2])
                for r in rows
            ]

    def import_from_csv(self, questions: list[QuestionCSV]) -> int:
        count = 0
        with self.cur() as cur:
            for q in questions:
                cur.execute(
                    "SELECT id FROM categories WHERE name = %s", (q.category,))
                category = cur.fetchone()
                if not category:
                    cur.execute(
                        "INSERT INTO categories (name) VALUES (%s) RETURNING id;",
                        (q.category,)
                    )
                    category = cur.fetchone()
                cur.execute(
                    """
                    INSERT INTO knowledge_base (category, question, answer)
                    VALUES (%s, %s, %s)
                    """,
                    (category[0], q.question, q.answer)
                )
                count += 1
        return count
