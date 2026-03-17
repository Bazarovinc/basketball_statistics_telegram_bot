import uuid
from abc import ABC, abstractmethod

from src.domain.dto.base import DivisionBaseSchema
from src.domain.dto.leagues_data.base import DivisionInfoBaseSchema


class IDivisionRepository(ABC):
    """Репозиторий для таблицы division."""

    @abstractmethod
    async def upsert(self, data: DivisionInfoBaseSchema, season_id: uuid.UUID) -> DivisionBaseSchema:
        """
        Вставляет дивизион или при конфликте (external_division_id, league) обновляет season_id.
        Возвращает актуальную запись.
        """
        raise NotImplementedError
