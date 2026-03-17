import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum


class LeagueSeasonBaseSchema(BaseSchema):
    """Схема таблицы league_season (связь сезона с лигой и external_season_id)."""

    league_season_id: uuid.UUID
    season_id: uuid.UUID
    external_season_id: str
    name: str
    league: LeagueTypeEnum
    create_date: datetime
    last_update_date: datetime
