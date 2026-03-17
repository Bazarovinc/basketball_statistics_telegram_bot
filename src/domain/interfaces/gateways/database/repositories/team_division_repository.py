import uuid
from abc import ABC, abstractmethod


class ITeamDivisionRepository(ABC):
    """Репозиторий для таблицы team_division."""

    @abstractmethod
    async def upsert(self, team_id: uuid.UUID, division_id: uuid.UUID) -> None:
        """
        Вставляет связь команда–дивизион или при конфликте (team_id, division_id) оставляет запись.
        """
        raise NotImplementedError
