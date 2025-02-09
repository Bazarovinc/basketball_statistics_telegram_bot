from common.domain.dto.league_reader_input import LeagueReaderInputSchema, LeagueTypeEnum
from src.constants import BCL_HOST


class BCLInputBaseSchema(LeagueReaderInputSchema):
    league_type: LeagueTypeEnum = LeagueTypeEnum.BCL
    _host: str = BCL_HOST
    # пока не буду парсить из урла ничего, т.к. в него надо будет просто сходить
