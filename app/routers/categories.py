from fastapi import APIRouter
from app.db.categories.usecases import Usecases, SelectInput
from app.db.categories.pg import Repo
from app.utils import safe_execute, ResponseModel
from app.model.category import Category

router = APIRouter(prefix='/categories', tags=["questions"])

repo = Repo()
uc = Usecases(repo)


@router.get('/', response_model=ResponseModel[list[Category]])
def get_categories(id: int = 0,
                   limit: int = 7,
                   offset: int = 0,
                   search: str = ""):
    return safe_execute(uc.get, SelectInput(
        limit=limit,
        offset=offset,
        search=search,
    ))
