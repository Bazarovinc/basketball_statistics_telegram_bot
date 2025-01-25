from common.domain.dto.league_reader_input import LeagueReaderInputSchema, LeagueTypeEnum


class BCLInputBaseSchema(LeagueReaderInputSchema):
    league_type: LeagueTypeEnum = LeagueTypeEnum.BCL
    # пока не буду парсить из урла ничего, т.к. в него надо будет просто сходить
