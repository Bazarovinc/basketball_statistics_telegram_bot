from abc import ABC, abstractmethod

from src.domain.dto.leagues_data.base import PlayerGameStatisticsInfoBaseSchema


class IPlayerGameStatisticsRepository(ABC):
    """Репозиторий для таблицы player_game_statistics."""

    @abstractmethod
    async def upsert(self, data: PlayerGameStatisticsInfoBaseSchema) -> None:
        """
        Вставляет статистику матча или при конфликте (player_profile_id, game_id)
        обновляет все статистические показатели.
        """
        raise NotImplementedError
