import uuid
from datetime import datetime

from pydantic import Field

from src.core.domain.dto import BaseSchema


class PlayerGameStatisticsBaseSchema(BaseSchema):
    """Схема таблицы player_game_statistics."""

    player_game_statistics_id: uuid.UUID
    player_profile_id: uuid.UUID
    game_id: uuid.UUID
    player_number: int | None = Field(None, ge=0, lt=100)
    total_points: int = Field(0, ge=0, le=1000)
    points_1: int = Field(0, ge=0, le=100)
    shots_1: int = Field(0, ge=0, le=100)
    points_2: int = Field(0, ge=0, le=100)
    shots_2: int = Field(0, ge=0, le=100)
    points_3: int = Field(0, ge=0, le=100)
    shots_3: int = Field(0, ge=0, le=100)
    assists: int = Field(0, ge=0, le=100)
    blocks: int = Field(0, ge=0, le=100)
    defence_rebounds: int = Field(0, ge=0, le=100)
    offence_rebounds: int = Field(0, ge=0, le=100)
    steals: int = Field(0, ge=0, le=100)
    turnovers: int = Field(0, ge=0, le=100)
    fouls: int = Field(0, ge=0, le=7)
    opponent_fouls: int = Field(0, ge=0, le=100)
    played_time_seconds: int = Field(0, ge=0, le=7200)
    plus_minus: int = Field(0, ge=-500, le=500)
    is_start: bool = False
    kpi: int = Field(0, ge=-500, le=500)
    create_date: datetime
