import uuid
from abc import ABC, abstractmethod


class IPlayerTeamRepository(ABC):
    """Репозиторий для таблицы player_team."""

    @abstractmethod
    async def upsert(self, player_profile_id: uuid.UUID, team_id: uuid.UUID) -> None:
        """
        Вставляет связь игрок–команда или при конфликте (player_profile_id, team_id) оставляет запись.
        """
        raise NotImplementedError
