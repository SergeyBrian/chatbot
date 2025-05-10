from app.db.categories.usecases import Interface, SelectInput
from app.db.connector import get_cursor
from app.model.category import Category


class Repo(Interface):
    def __init__(self):
        self.cur = get_cursor

    def create(self, msg: Category) -> Category:
        with self.cur() as cur:
            cur.execute(
                """
                INSERT INTO categories (name)
                VALUES (%s)
                RETURNING id, name;
                """,
                (msg.name,),
            )
            row = cur.fetchone()
            # возвращаем Pydantic-модель с тем же именем и реальным id
            return Category(id=row[0], name=row[1])

    def get(self, req: SelectInput) -> list[Category]:
        with self.cur() as cur:
            if req.search:
                # ищем по подстроке, case-insensitive
                pattern = f"%{req.search}%"
                cur.execute(
                    """
                    SELECT id, name
                    FROM categories
                    WHERE name ILIKE %s
                    ORDER BY name
                    LIMIT %s
                    OFFSET %s;
                    """,
                    (pattern, req.limit, req.offset),
                )
            else:
                # без фильтрации
                cur.execute(
                    """
                    SELECT id, name
                    FROM categories
                    ORDER BY name
                    LIMIT %s
                    OFFSET %s;
                    """,
                    (req.limit, req.offset),
                )

            rows = cur.fetchall()
            return [Category(id=r[0], name=r[1]) for r in rows]
