import uuid
from abc import ABC, abstractmethod

from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.leagues_data.base import PlayerProfileInfoBaseSchema


class IPlayerProfileRepository(ABC):
    """Репозиторий для таблицы player_profile."""

    @abstractmethod
    async def create(self, data: PlayerProfileInfoBaseSchema, user_id: uuid.UUID) -> None:
        """Создаёт запись профиля игрока."""
        raise NotImplementedError

    @abstractmethod
    async def is_exists(self, user_id: uuid.UUID, league: LeagueTypeEnum) -> bool:
        """Проверяет наличие профиля игрока по user_id и league."""
        raise NotImplementedError
