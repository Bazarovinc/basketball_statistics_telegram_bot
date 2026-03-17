from src.core.domain.dto import BaseSchema


class BCLPlayerProfilePageSchema(BaseSchema):
    """Данные, извлечённые со страницы профиля игрока BCL."""

    team_id: int
    season_ids: list[int]
