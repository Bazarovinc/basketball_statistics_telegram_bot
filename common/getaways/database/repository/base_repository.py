from typing import Generic, Type

from sqlalchemy.ext.asyncio import AsyncSession

from common.domain.dto import Schema
from common.getaways.database.base import ModelType
from common.getaways.database.repository.interfaces import BaseRepositoryProtocol


class BaseRepository(BaseRepositoryProtocol, Generic[ModelType, Schema]):
    """
    Базовый репозиторий

    Attributes:
        model (Type[ModelType]): модель (таблица в БД)
        schema (Type[Schema]): схема
    """

    model: Type[ModelType]
    schema: Type[Schema]

    def __init__(self, session: AsyncSession) -> None:
        """
        Args:
            session: сессия с БД
        """
        self._session: AsyncSession = session
