from fastapi import APIRouter
from app.db.questions.usecases import Usecases, SelectInput
from app.db.questions.pg import Repo
from app.utils import safe_execute, ResponseModel
from app.model.question import Question

router = APIRouter(prefix='/questions', tags=["questions"])

repo = Repo()
uc = Usecases(repo)


@router.get('/', response_model=ResponseModel[list[Question]])
def get_questions(
        limit: int = 7,
        offset: int = 0,
        category_id: int = 0,
        search: str = ""):
    return safe_execute(uc.get, SelectInput(
        limit=limit,
        offset=offset,
        search=search,
    ))


@router.post('/', response_model=ResponseModel[Question])
def create_question(question: Question):
    return safe_execute(uc.create, question)
