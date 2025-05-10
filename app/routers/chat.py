from fastapi import APIRouter
from app.db.messages.usecases import Usecases, SelectInput
from app.db.messages.pg import Repo
from app.model.message import Message

router = APIRouter(prefix='/chat')

msgRepo = Repo()
msgUc = Usecases(msgRepo)


@router.post('/{id}/message')
def post_message(id: int, text: str):
    return {'resp': msgUc.create(msg=Message(chat_id=id, content=text))}


@router.get('/{id}')
def get_chat(id: int):
    return {'resp': msgUc.get(req=SelectInput(chat_id=id))}
