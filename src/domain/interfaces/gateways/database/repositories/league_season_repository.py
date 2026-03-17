import uuid
from abc import ABC, abstractmethod

from src.domain.dto.leagues_data.base import LeagueSeasonInfoBaseSchema


class ILeagueSeasonRepository(ABC):
    """Репозиторий для таблицы league_season."""

    @abstractmethod
    async def upsert(self, season_id: uuid.UUID, data: LeagueSeasonInfoBaseSchema) -> None:
        """
        Вставляет запись league_season или при конфликте (external_season_id, league)
        обновляет только имя сезона (name).
        """
        raise NotImplementedError
