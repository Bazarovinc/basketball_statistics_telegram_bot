from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum


class FastStatisticsOutputSchema(BaseSchema):
    league: LeagueTypeEnum = LeagueTypeEnum.MLBL
    images: tuple[tuple[bytes, str], ...]
    username: str
