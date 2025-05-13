from fastapi import APIRouter
from app.db.users.usecases import Usecases, SelectInput
from app.db.users.pg import Repo
from app.model.user import User
from app.utils import safe_execute, ResponseModel

router = APIRouter(prefix='/user', tags=["users"])

repo = Repo()
uc = Usecases(repo)


@router.post('/', response_model=ResponseModel[User])
def create_user(id: int, username: str):
    return safe_execute(uc.create, User(session_id=id, name=username))


@router.get('/', response_model=ResponseModel[User])
def get_user(id: int = 0, username: str = ""):
    return safe_execute(uc.get, req=SelectInput(user_id=id, username=username))
