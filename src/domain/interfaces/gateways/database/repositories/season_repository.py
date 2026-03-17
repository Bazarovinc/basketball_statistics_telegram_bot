from abc import ABC, abstractmethod

from src.domain.dto.base import SeasonBaseSchema
from src.domain.dto.leagues_data.base import SeasonInfoBaseSchema


class ISeasonRepository(ABC):
    """Репозиторий для таблицы season."""

    @abstractmethod
    async def upsert(self, data: SeasonInfoBaseSchema) -> SeasonBaseSchema:
        """
        Вставляет сезон или при конфликте по (start_year, end_year) обновляет
        last_update_date и current_season. Возвращает актуальную запись сезона.
        Связь сезон–лига (external_season_id) хранится в таблице league_season.
        """
        raise NotImplementedError
