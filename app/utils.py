from typing import Callable, Any


def safe_execute(func: Callable[..., Any], *args, **kwargs) -> dict:
    try:
        result = func(*args, **kwargs)
        return {"msg": result, "status": "OK"}
    except Exception as e:
        return {"msg": str(e), "status": "ERR"}
