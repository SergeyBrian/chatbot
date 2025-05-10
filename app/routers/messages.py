from fastapi import APIRouter
from app.db.messages.usecases import Usecases, SelectInput, UpdateInput
from app.db.messages.pg import Repo
from app.model.message import Message
from app.utils import safe_execute, ResponseModel

router = APIRouter(prefix='/message')

repo = Repo()
uc = Usecases(repo)


@router.post('/', response_model=ResponseModel[Message])
def post_message(id: int, text: str):
    return safe_execute(uc.create, Message(chat_id=id, content=text))


@router.get('/', response_model=ResponseModel[list[Message]])
def get_messages(id: int):
    return safe_execute(uc.get, req=SelectInput(chat_id=id))


@router.patch('/{msg_id}', response_model=ResponseModel[Message])
def update_message(msg_id: int, req: UpdateInput):
    req.id = msg_id
    return safe_execute(uc.update, req)
