from fastapi import APIRouter
from app.db.chats.usecases import Usecases, SelectInput
from app.db.chats.pg import Repo
from app.model.chat import Chat
from app.utils import safe_execute, ResponseModel
from app.routers.messages import router as msgRouter

router = APIRouter(prefix='/chat', tags=["chat"])
router.include_router(msgRouter, prefix='/{id}')

repo = Repo()
uc = Usecases(repo)


@router.get('/', response_model=ResponseModel[list[Chat]])
def get_chats():
    return {}
