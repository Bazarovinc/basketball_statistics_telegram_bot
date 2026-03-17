from src.core.domain.dto import BaseSchema
from src.domain.dto.leagues_data.base import (
    DivisionInfoBaseSchema,
    GameInfoBaseSchema,
    PlayerGameStatisticsInfoBaseSchema,
    PlayerProfileInfoBaseSchema,
    SeasonInfoBaseSchema,
    TeamInfoBaseSchema,
)
from src.domain.dto.leagues_data.base.full_statistics import FullStatisticsBaseSchema


class MLBLPlayerProfileInfoSchema(PlayerProfileInfoBaseSchema):
    pass


class MLBLTeamSeasonResponseSchema(BaseSchema):
    pass


class MLBLTeamInfoSchema(TeamInfoBaseSchema):
    pass


class MLBLDivisionInfoSchema(DivisionInfoBaseSchema):
    pass


class MLBLSeasonInfoSchema(SeasonInfoBaseSchema):
    pass


class MLBLPlayerGameStatisticsInfoSchema(PlayerGameStatisticsInfoBaseSchema):
    pass


class MLBLGameInfoSchema(GameInfoBaseSchema):
    pass


class MLBLFullStatisticsSchema(FullStatisticsBaseSchema):
    pass
