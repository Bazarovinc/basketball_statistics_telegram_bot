import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema
from src.core.domain.dto.league_reader_input import LeagueTypeEnum


class TeamBaseSchema(BaseSchema):
    """Схема таблицы team"""

    team_id: uuid.UUID
    external_team_id: str
    team_name: str
    team_short_name: str | None = None
    team_name_abc: str | None = None
    region: str | None = None
    logo: str | None = None
    league: LeagueTypeEnum | None = None
    create_date: datetime
