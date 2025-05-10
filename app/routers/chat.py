from fastapi import APIRouter

router = APIRouter('/chat')


@router.post('/message')
def post_message():
    return {'resp': 'OK'}
