from pydantic import AnyHttpUrl, model_validator

from common.domain.dto.league_reader_input import LeagueReaderInputSchema, LeagueTypeEnum
from src.constants import MLBL_PLAYER_PATH_PARAM, MLBL_TEAM_PATH_PARAM


class MLBLInputBaseSchema(LeagueReaderInputSchema):
    league_type: LeagueTypeEnum = LeagueTypeEnum.MLBL
    player_comp_id: int | str
    team_comp_id: int | str | None = None

    @staticmethod
    def _get_comp_id(values: list[tuple[str, str]]) -> int:
        for param, value in values:
            if param == "compId":
                return int(value)
        raise ValueError("Отсутствует query-параметр compId")

    @model_validator(mode="before")
    def parse_urls(cls, values: dict) -> dict:
        player_url = values.get("player_url")
        team_url = values.get("team_url")
        if player_url:
            player_url = AnyHttpUrl(player_url)
            path_params = player_url.path.split("/")
            if path_params[-2] != MLBL_PLAYER_PATH_PARAM and not path_params[-1].isdigit():
                raise ValueError("path-параметры не соответствуют")
            values["player_id"] = int(path_params[-1])
            if values["player_id"] <= 0:
                raise ValueError("некорректный player_id")
            values["player_comp_id"] = cls._get_comp_id(player_url.query_params())
        if team_url:
            team_url = AnyHttpUrl(team_url)
            path_params = player_url.path.split("/")
            if path_params[-2] != MLBL_TEAM_PATH_PARAM and not path_params[-1].isdigit():
                raise ValueError("path-параметры не соответствуют")
            values["team_id"] = int(path_params[-1])
            values["team_comp_id"] = cls._get_comp_id(team_url.query_params())
        return values


class MLBLFullInputSchema(MLBLInputBaseSchema):
    team_url: AnyHttpUrl
    team_id: int | str
    team_comp_id: int | str
