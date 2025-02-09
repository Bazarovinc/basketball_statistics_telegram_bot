from pydantic import AnyHttpUrl, model_validator

from common.domain.dto.league_reader_input import LeagueReaderInputSchema, LeagueTypeEnum
from src.constants import ABL_HOST, ABL_PLAYER_PATH_PARAM


class ABLInputBaseSchema(LeagueReaderInputSchema):
    _host: str = ABL_HOST
    league_type: LeagueTypeEnum = LeagueTypeEnum.ABL
    season_id: int

    @staticmethod
    def _get_comp_id(values: list[tuple[str, str]]) -> int:
        for param, value in values:
            if param == "seasonId":
                return int(value)
        raise ValueError("Отсутствует query-параметр compId")

    @model_validator(mode="before")
    def parse_urls(cls, values: dict) -> dict:
        player_url = values.get("player_url")
        if player_url:
            player_url = AnyHttpUrl(player_url)
            path_params = player_url.path.split("/")
            if path_params[-2] != ABL_PLAYER_PATH_PARAM and not path_params[-1].isdigit():
                raise ValueError("path-параметры не соответствуют")
            values["player_id"] = int(path_params[-1])
            values["season_id"] = cls._get_comp_id(player_url.query_params())
        return values
