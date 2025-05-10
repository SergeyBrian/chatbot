from typing import Callable, Any, TypeVar, Generic
from pydantic import BaseModel


def safe_execute(func: Callable[..., Any], *args, **kwargs) -> dict:
    try:
        result = func(*args, **kwargs)
        return {"msg": result, "status": "OK"}
    except Exception as e:
        return {"msg": str(e), "status": "ERR"}


T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    msg: T
    status: str
