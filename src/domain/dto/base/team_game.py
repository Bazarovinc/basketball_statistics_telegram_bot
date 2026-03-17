import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema
from src.domain.enums import TeamPositionEnum


class TeamGameBaseSchema(BaseSchema):
    """Схема таблицы team_game."""

    team_game_id: uuid.UUID
    team_id: uuid.UUID
    game_id: uuid.UUID
    team_position: TeamPositionEnum
    create_date: datetime
