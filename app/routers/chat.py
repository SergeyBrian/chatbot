from fastapi import APIRouter
from app.db.chats.usecases import Usecases, SelectInput, UpdateInput
from app.db.chats.pg import Repo
from app.model.chat import Chat
from app.utils import safe_execute, ResponseModel
from app.routers.messages import router as msgRouter

router = APIRouter(prefix='/chat', tags=["chat"])
router.include_router(msgRouter, prefix='/{id}')

repo = Repo()
uc = Usecases(repo)


@router.get('/', response_model=ResponseModel[list[Chat]])
def get_chats(limit: int = 25, offset: int = 0):
    return safe_execute(uc.get, req=SelectInput(limit=limit, offset=offset))


@router.post('/', response_model=ResponseModel[Chat])
def create_chat(user_id: int):
    return safe_execute(uc.create, Chat(user_id=user_id))


@router.patch('/{id}', response_model=ResponseModel[Chat])
def update_chat(id: int, chat: UpdateInput):
    chat.id = id
    return safe_execute(uc.update, chat)
