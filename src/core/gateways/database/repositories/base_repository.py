from typing import Generic, TypeVar

import asyncpg

from src.core.domain.dto.base import BaseSchema, Schema
from src.core.domain.interfaces.gateways.database.interfaces import BaseRepositoryInterface

SchemaT = TypeVar("SchemaT", bound=BaseSchema)


class BaseRepository(BaseRepositoryInterface, Generic[Schema]):
    """
    Базовый репозиторий для работы с БД через asyncpg.
    Без SQLAlchemy: имя таблицы задаётся строкой, список колонок берётся из схемы.

    Attributes:
        table_name: имя таблицы в БД (строка, задаётся в наследнике).
        schema: Pydantic-схема для сериализации и список допустимых колонок (model_fields).
    """

    table_name: str
    schema: type[Schema]

    def __init__(self, connection: asyncpg.Connection) -> None:
        self._connection: asyncpg.Connection = connection
