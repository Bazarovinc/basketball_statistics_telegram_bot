import uuid
from datetime import datetime

from src.core.domain.dto import BaseSchema


class PlayerTeamBaseSchema(BaseSchema):
    """Схема таблицы player_team (composite PK: player_profile_id, team_id)."""

    player_profile_id: uuid.UUID
    team_id: uuid.UUID
    create_date: datetime
