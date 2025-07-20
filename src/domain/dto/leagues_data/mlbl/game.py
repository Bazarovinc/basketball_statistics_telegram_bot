from datetime import datetime

from pydantic import Field, field_validator, model_validator

from common.domain.dto import BaseSchema
from common.utils.date_parser import parse_date_from_timestamp
from src.constants.fields import FIELDS_TO_ZERO
from src.enums import MLBLGameStatusEnum


class MLBLGameResponseSchema(BaseSchema):
    game_id: int = Field(..., alias="GameID")
    game_number: str = Field(..., alias="GameNumber")
    game_date: datetime = Field(..., alias="GameDateTimeMoscow")
    game_status: MLBLGameStatusEnum = Field(..., alias="GameStatus")
    left_league_team_id: int = Field(..., alias="TeamAid")
    right_league_team_id: int = Field(..., alias="TeamBid")
    left_team_name: str = Field(..., alias="TeamNameAru")
    right_team_name: str = Field(..., alias="TeamNameBru")
    left_team_score: int = Field(..., alias="ScoreA")
    right_team_score: int = Field(..., alias="ScoreB")
    game_place: str = Field(..., alias="ArenaRu")
    competition_type: str = Field(..., alias="CompNameRu")
    division_name: str = Field(..., alias="LeagueNameRu")
    division_season: str = Field(..., alias="LeagueShortNameRu")

    @field_validator("game_date", mode="before")
    def validate_datetime(cls, value: str | datetime) -> datetime:
        if isinstance(value, str):
            return parse_date_from_timestamp(value)
        return value


class MLBLPlayerStatisticResponseSchema(BaseSchema):
    player_id: int = Field(..., alias="PersonID", description="ID игрока")
    player_number: int = Field(..., alias="PlayerNumber", description="Игровой номер игрока")
    total_points: int | None = Field(..., alias="Points", description="Набрано очков за игру")
    points_1: int | None = Field(..., alias="Goal1", description="Забито штрафных")
    shots_1: int | None = Field(..., alias="Shot1", description="Брошено штрафных")
    points_2: int | None = Field(..., alias="Goal2", description="Забито 2-ух очковых")
    shots_2: int | None = Field(..., alias="Shot2", description="Брошено 2-ух очковых")
    points_3: int | None = Field(..., alias="Goal3", description="Забито 3-ех очковых")
    shots_3: int | None = Field(..., alias="Shot3", description="Брошено 3-ех очковых")
    assists: int | None = Field(..., alias="Assist", description="Голевые передачи")
    blocks: int | None = Field(..., alias="Blocks", description="Блок-шоты")
    defence_rebounds: int | None = Field(..., alias="DefRebound", description="Подборы в защите")
    offence_rebounds: int | None = Field(..., alias="OffRebound", description="Подборы в нападении")
    steals: int | None = Field(..., alias="Steal", description="Перехваты")
    turnovers: int | None = Field(..., alias="Turnover", description="Потери")
    fouls: int | None = Field(..., alias="Foul", description="Фолы")
    opponent_fouls: int | None = Field(..., alias="OpponentFoul", description="Фолы соперника")
    played_time: str | None = Field(..., alias="PlayedTime", description="Сыграно времени")
    plus_minus: int | None = Field(..., alias="PlusMinus", description="+/-")
    is_start: bool | None = Field(..., alias="IsStart", description="Стартовая 5")
    kpi: int | None = Field(None, description="Коэффициент полезности игрока (КПИ)")

    @field_validator(
        *FIELDS_TO_ZERO,
        mode="after",
    )
    def set_zero(cls, value: int | None) -> int:
        if value is None:
            return 0
        return value

    @model_validator(mode="after")
    def calculate_kpi(self) -> "MLBLPlayerStatisticResponseSchema":
        self.kpi = (
            self.total_points
            + self.defence_rebounds
            + self.offence_rebounds
            + self.assists
            + self.steals
            + self.blocks
            + self.opponent_fouls
            - (self.shots_1 - self.points_1)
            - (self.shots_2 - self.points_2)
            - (self.shots_3 - self.points_3)
            - self.turnovers
            - self.fouls
        )
        return self


class MLBLTeamStatisticResponseSchema(BaseSchema):
    team_number: int = Field(..., alias="TeamNumber")
    team_id: int = Field(..., alias="TeamID")
    score: int | None = Field(..., alias="Score")
    shot_1: int | None = Field(..., alias="Shot1")
    goal_1: int | None = Field(..., alias="Goal1")
    shot_2: int | None = Field(..., alias="Shot2")
    goal_2: int | None = Field(..., alias="Goal2")
    shot_3: int | None = Field(..., alias="Shot3")
    goal_3: int | None = Field(..., alias="Goal3")
    assists: int | None = Field(None, alias="Assists")
    blocks: int | None = Field(None, alias="Blocks")
    defence_rebounds: int | None = Field(None, alias="DefRebound")
    offence_rebounds: int | None = Field(None, alias="OffRebound")
    steals: int | None = Field(None, alias="Steal")
    turnovers: int | None = Field(None, alias="Turnover")
    fouls: int | None = Field(None, alias="Foul")
    opponent_fouls: int | None = Field(None, alias="OpponentFoul")
    players: list[MLBLPlayerStatisticResponseSchema] = Field(..., alias="Players")


class MLBLGameStatisticResponseSchema(BaseSchema):
    game_status: MLBLGameStatusEnum = Field(..., alias="GameStatus")
    teams: list[MLBLTeamStatisticResponseSchema] = Field(..., alias="GameTeams")
