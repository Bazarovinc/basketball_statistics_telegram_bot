from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, TypeVar, get_type_hints

from pydantic import TypeAdapter, ValidationError

from src.core.exceptions.utils_exceptions import SerializationException

RT = TypeVar("RT")  # return type


def _serialize_result(results: Any, return_type: type[RT]) -> RT:
    if results:
        if not return_type:
            raise ValueError("Установите возвращаемый тип функции")
        # asyncpg Record и другие mapping-подобные объекты приводим к dict
        if hasattr(results, "keys") and not isinstance(results, dict):
            results = dict(results)
        if isinstance(results, dict):
            return return_type(**results)
        try:
            return TypeAdapter(return_type).validate_python(results)
        except ValidationError as ex:
            raise SerializationException(ex) from ex
    return results


def serialize(func: Callable[..., RT]) -> Callable[..., RT]:
    """
    Сериализация ответа функции, используя type hints

    Parameters:
        func: декорируемая функция

    Raises:
        ValueError: если возвращаемый тип функции не установлен
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> RT:
        results = func(*args, **kwargs)
        return_type = get_type_hints(func).get("return")
        return _serialize_result(results, return_type)

    return wrapper


def async_serialize(
    func: Callable[..., Coroutine[Any, Any, RT]],
) -> Callable[[Any, Any], Coroutine[Any, Any, RT]]:
    """
    Сериализация ответа функции, используя type hints

    Parameters:
        func: декорируемая функция

    Raises:
        ValueError: если возвращаемый тип функции не установлен
    """

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> RT:
        results = await func(*args, **kwargs)
        return_type = get_type_hints(func).get("return")
        return _serialize_result(results, return_type)

    return wrapper
