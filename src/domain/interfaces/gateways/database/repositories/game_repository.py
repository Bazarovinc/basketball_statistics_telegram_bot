from abc import ABC, abstractmethod

from src.domain.dto.base import GameBaseSchema
from src.domain.dto.leagues_data.base import GameInfoBaseSchema


class IGameRepository(ABC):
    """Репозиторий для таблицы game."""

    @abstractmethod
    async def upsert(self, data: GameInfoBaseSchema) -> GameBaseSchema:
        """
        Вставляет игру или при конфликте (game_id) обновляет
        game_date, left_team_points, right_team_points, left_team_quarters_points,
        right_team_quarters_points, game_status, left_team_id, right_team_id.
        division_id и team_id при отсутствии разрешаются по external_*_id.
        """
        raise NotImplementedError
