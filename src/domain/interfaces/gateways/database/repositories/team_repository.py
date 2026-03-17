from abc import ABC, abstractmethod

from src.domain.dto.base import TeamBaseSchema
from src.domain.dto.leagues_data.base import TeamInfoBaseSchema


class ITeamRepository(ABC):
    """Репозиторий для таблицы team."""

    @abstractmethod
    async def upsert(self, data: TeamInfoBaseSchema) -> TeamBaseSchema:
        """
        Вставляет команду или при конфликте (external_team_id, league) обновляет поля.
        Возвращает актуальную запись.
        """
        raise NotImplementedError
