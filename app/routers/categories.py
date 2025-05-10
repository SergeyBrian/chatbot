from fastapi import APIRouter
from app.db.categories.usecases import Usecases, SelectInput
from app.db.categories.pg import Repo
from app.utils import safe_execute

router = APIRouter(prefix='/categories')

repo = Repo()
uc = Usecases(repo)


@router.get('/')
def get_categories(id: int, limit: int = 7, offset: int = 0, search: str = ""):
    return safe_execute(uc.get, SelectInput(
        limit=limit,
        offset=offset,
        search=search,
    ))
