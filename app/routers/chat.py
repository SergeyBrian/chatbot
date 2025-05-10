from fastapi import APIRouter
from app.db.messages.usecases import Usecases, SelectInput
from app.db.messages.pg import Repo
from app.model.message import Message
from app.utils import safe_execute, ResponseModel

router = APIRouter(prefix='/chat', tags=["chat"])

repo = Repo()
uc = Usecases(repo)


@router.post('/{id}/message', response_model=ResponseModel[Message])
def post_message(id: int, text: str):
    return safe_execute(uc.create, Message(chat_id=id, content=text))


@router.get('/{id}/message', response_model=ResponseModel[list[Message]])
def get_messages(id: int):
    return safe_execute(uc.get, req=SelectInput(chat_id=id))
