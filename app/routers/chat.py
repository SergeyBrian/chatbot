from fastapi import APIRouter
from app.db.messages.usecases import Usecases

router = APIRouter(prefix='/chat')


@router.post('/{id}/message')
def post_message(id: int, text: str):
    return {'resp': 'OK'}


@router.get('/{id}')
def get_chat(id: int):
    return {'chat': 'sosal'}
