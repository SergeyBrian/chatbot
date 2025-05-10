from fastapi import APIRouter

router = APIRouter(prefix='/chat')


@router.post('/message')
def post_message():
    return {'resp': 'OK'}


@router.get('/{id}')
def get_chat(id: int):
    return {'chat': 'sosal'}
