from datetime import timedelta
from decimal import Decimal
from functools import cached_property
from typing import TypeVar

from pydantic import computed_field

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum


class StatisticsPresenterBaseSchema(BaseSchema):
    game_info: str | None = None
    total_points: int | None
    points_1: int | None
    shots_1: int | None
    points_2: int | None
    shots_2: int | None
    points_3: int | None
    shots_3: int | None
    assists: int | None
    blocks: int | None
    defence_rebounds: int | None
    offence_rebounds: int | None
    steals: int | None
    turnovers: int | None
    fouls: int | None
    opponent_fouls: int | None
    played_time: str | None
    plus_minus: int | None
    is_start: bool | None
    kpi: int | None

    @computed_field
    @cached_property
    def played_time_seconds(self) -> timedelta:
        minutes, seconds = self.played_time.split(":") if self.played_time else (0, 0)
        return timedelta(minutes=int(minutes), seconds=int(seconds))


class PlayerShortInfoBaseSchema(BaseSchema):
    first_name: str
    last_name: str

    @cached_property
    def username(self) -> str:
        return self.last_name + " " + self.first_name


class PlayerStatisticsPresenterBaseSchema(BaseSchema):
    league: LeagueTypeEnum
    player_info: PlayerShortInfoBaseSchema
    statistics_per_game: tuple[StatisticsPresenterBaseSchema]

    @computed_field
    @cached_property
    def username(self) -> str:
        return self.player_info.username

    @computed_field
    @cached_property
    def total_games(self) -> int:
        return len(self.statistics_per_game)

    @computed_field
    @cached_property
    def total_points(self) -> int:
        return sum(stat.total_points or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_total_points(self) -> Decimal:
        return round(Decimal(self.total_points / self.total_games), 1)

    @computed_field
    @cached_property
    def total_points_1(self) -> int:
        return sum(stat.points_1 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def total_shots_1(self) -> int:
        return sum(stat.shots_1 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def percent_shots_1(self) -> Decimal:
        return round(Decimal(self.total_points_1 / self.total_shots_1 * 100), 1)

    @computed_field
    @cached_property
    def total_points_2(self) -> int:
        return sum(stat.points_2 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def total_shots_2(self) -> int:
        return sum(stat.shots_2 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def percent_shots_2(self) -> Decimal:
        return round(Decimal(self.total_points_2 / self.total_shots_2 * 100), 1)

    @computed_field
    @cached_property
    def total_points_3(self) -> int:
        return sum(stat.points_3 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def total_shots_3(self) -> int:
        return sum(stat.shots_3 or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def percent_shots_3(self) -> Decimal:
        return round(Decimal(self.total_points_3 / self.total_shots_3) * 100, 1)

    @computed_field
    @cached_property
    def total_assists(self) -> int:
        return sum(stat.assists or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_assists(self) -> Decimal:
        return round(Decimal(self.total_assists / self.total_games), 1)

    @computed_field
    @cached_property
    def total_steals(self) -> int:
        return sum(stat.steals or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_steals(self) -> Decimal:
        return round(Decimal(self.total_steals / self.total_games), 1)

    @computed_field
    @cached_property
    def total_turnovers(self) -> int:
        return sum(stat.turnovers or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_turnovers(self) -> Decimal:
        return round(Decimal(self.total_turnovers / self.total_games), 1)

    @computed_field
    @cached_property
    def total_blocks(self) -> int:
        return sum(stat.blocks or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_blocks(self) -> Decimal:
        return round(Decimal(self.total_blocks / self.total_games), 1)

    @computed_field
    @cached_property
    def total_fouls(self) -> int:
        return sum(stat.fouls or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_fouls(self) -> Decimal:
        return round(Decimal(self.total_fouls / self.total_games), 1)

    @computed_field
    @cached_property
    def total_opponent_fouls(self) -> int:
        return sum(stat.opponent_fouls or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_opponent_fouls(self) -> Decimal:
        return round(Decimal(self.total_opponent_fouls / self.total_games), 1)

    @computed_field
    @cached_property
    def total_offence_rebounds(self) -> int:
        return sum(stat.offence_rebounds or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_offence_rebounds(self) -> Decimal:
        return round(Decimal(self.total_offence_rebounds / self.total_games), 1)

    @computed_field
    @cached_property
    def total_defence_rebounds(self) -> int:
        return sum(stat.defence_rebounds or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_defence_rebounds(self) -> Decimal:
        return round(Decimal(self.total_defence_rebounds / self.total_games), 1)

    @computed_field
    @cached_property
    def total_rebounds(self) -> int:
        return self.total_defence_rebounds + self.total_offence_rebounds

    @computed_field
    @cached_property
    def mean_rebounds(self) -> Decimal:
        return round(Decimal(self.total_rebounds / self.total_games), 1)

    @computed_field
    @cached_property
    def total_start(self) -> int:
        return sum(stat.is_start or 0 for stat in self.statistics_per_game)

    @cached_property
    def _total_played_time_seconds(self) -> int:
        return int(sum(stat.played_time_seconds.total_seconds() for stat in self.statistics_per_game))

    @computed_field
    @cached_property
    def total_played_time(self) -> str:
        minutes = self._total_played_time_seconds // 60
        seconds = self._total_played_time_seconds % 60
        return f"{minutes}:{seconds}"

    @computed_field
    @cached_property
    def mean_played_time(self) -> str:
        minutes = int(self._total_played_time_seconds / self.total_games) // 60
        seconds = int(self._total_played_time_seconds / self.total_games) % 60
        return f"{minutes}:{seconds}"

    @computed_field
    @cached_property
    def total_kpi(self) -> int:
        return sum(stat.kpi or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_kpi(self) -> Decimal:
        return round(Decimal(self.total_kpi / self.total_games), 1)

    @computed_field
    @cached_property
    def total_plus_minus(self) -> int:
        return sum(stat.plus_minus or 0 for stat in self.statistics_per_game)

    @computed_field
    @cached_property
    def mean_plus_minus(self) -> Decimal:
        return round(Decimal(self.total_plus_minus / self.total_games), 1)


StatisticsPresenterSchema = TypeVar("StatisticsPresenterSchema", bound=StatisticsPresenterBaseSchema)
PlayerStatisticsPresenterSchema = TypeVar("PlayerStatisticsPresenterSchema", bound=PlayerStatisticsPresenterBaseSchema)
