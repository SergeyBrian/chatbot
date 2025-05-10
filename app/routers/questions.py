from fastapi import APIRouter
from app.db.questions.usecases import Usecases, SelectInput
from app.db.questions.pg import Repo
from app.utils import safe_execute
from app.model.question import Question

router = APIRouter(prefix='/questions', tags=["questions"])

repo = Repo()
uc = Usecases(repo)


# @router.get('/')
# def get_categories(id: int, limit: int = 7, offset: int = 0, search: str = ""):
#     return safe_execute(uc.get, SelectInput(
#         limit=limit,
#         offset=offset,
#         search=search,
#     ))
#
#
# @router.post('/')
# def create_category(name: str):
#     return safe_execute(uc.create, Question(name=name))
