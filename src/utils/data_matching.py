from collections import defaultdict

from loguru import logger

from src.constants import BCL_AUTUMN_SEASON_NAME, BCL_SPRING_SEASON_NAME, SEASON_NAME_TEMPLATE
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.core.exceptions.parsers_exceptions import ServerNotAvailableException
from src.domain.dto.leagues_data.abl.fast_statistics import (
    ABLFSGameInfoResponseSchema,
    ABLGameStatisticsSchema,
    ABLPlayerFastStatisticsResponseSchema,
    ABLPlayerGameInfoResponseSchema,
)
from src.domain.dto.leagues_data.abl.full_statistics import (
    ABLDivisionInfoSchema,
    ABLGameInfoSchema,
    ABLLeagueSeasonInfoSchema,
    ABLPlayerGameStatisticsInfoSchema,
    ABLPlayerProfileInfoSchema,
    ABLSeasonInfoSchema,
    ABLTeamInfoSchema,
    ABLTeamSeasonResponseSchema,
)
from src.domain.dto.leagues_data.bcl.full_statistics import (
    BCLLeagueSeasonInfoSchema,
    BCLPlayerSeasonSchema,
    BCLSeasonInfoSchema,
)


def match_abl_player_statistics(
    player_profile: ABLPlayerFastStatisticsResponseSchema,
    games_info: list[ABLFSGameInfoResponseSchema],
    games_players_info: tuple[list[ABLPlayerGameInfoResponseSchema], ...],
    games_players_statistics: tuple[list[ABLGameStatisticsSchema], ...],
) -> list[ABLGameStatisticsSchema]:
    player_games_statistics: list[ABLGameStatisticsSchema] = []
    for game_players_info, game_players_statistics, game_info in zip(
        games_players_info, games_players_statistics, games_info
    ):
        need_player: ABLPlayerGameInfoResponseSchema | None = None
        for player_info in game_players_info:
            if not player_info:
                logger.error("Данные от лиги не получены")
                raise ServerNotAvailableException()
            if player_info.player_id == player_profile.user_id:
                need_player = player_info
                break
        for players_statistics in game_players_statistics:
            if not players_statistics:
                logger.error("Данные от лиги не получены")
                raise ServerNotAvailableException()
            if need_player.id == players_statistics.game_user_id:
                players_statistics.game_info = game_info.game_info
                player_games_statistics.append(players_statistics)
    return player_games_statistics[::-1]


def match_abl_full_player_games(
    player_profile: ABLPlayerProfileInfoSchema,
    games_info: list[ABLGameInfoSchema],
    games_players_info: tuple[list[ABLPlayerGameInfoResponseSchema], ...],
    games_players_statistics: tuple[list[ABLGameStatisticsSchema], ...],
) -> None:
    for game_players_info, game_players_statistics, game_info in zip(
        games_players_info, games_players_statistics, games_info
    ):
        need_player: ABLPlayerGameInfoResponseSchema | None = None
        for player_info in game_players_info:
            if not player_info:
                logger.error("Данные от лиги не получены")
                raise ServerNotAvailableException()
            if player_info.player_id == player_profile.player_id:
                need_player = player_info
                player_profile.player_numbers.append(need_player.player_number)
                break
        if need_player is None:
            continue
        for players_statistics in game_players_statistics:
            if not players_statistics:
                logger.error("Данные от лиги не получены")
                raise ServerNotAvailableException()
            if need_player.id == players_statistics.game_user_id:
                players_statistics.player_number = need_player.player_number
                game_info.player_statistics = ABLPlayerGameStatisticsInfoSchema(
                    **players_statistics.model_dump(),
                    player_profile_id=player_profile.player_profile_id,
                    game_id=game_info.game_id,
                )
                break


def build_abl_seasons_from_team_response(
    team_season_responses: list[ABLTeamSeasonResponseSchema],
) -> list[ABLSeasonInfoSchema]:
    """Собирает список ABLSeasonInfoSchema из ответа API (ABLTeamSeasonResponseSchema).

    Группирует записи по сезону; в каждом сезоне — список дивизионов; в каждом дивизионе — список команд.
    Одна запись ответа = участие одной команды в одном турнире (дивизионе) в одном сезоне.
    В одном дивизионе может быть несколько команд (несколько записей с одним division_id).
    """
    by_season: defaultdict[str, list[ABLTeamSeasonResponseSchema]] = defaultdict(list)
    for item in team_season_responses:
        by_season[item.season_id].append(item)

    result: list[ABLSeasonInfoSchema] = []
    for season_id_str, items in by_season.items():
        first = items[0]
        # Группируем по дивизиону: в одном дивизионе может быть несколько команд
        by_division: defaultdict[str, list[ABLTeamSeasonResponseSchema]] = defaultdict(list)
        for item in items:
            by_division[item.division_id].append(item)

        divisions: list[ABLDivisionInfoSchema] = []
        for division_id, division_items in by_division.items():
            teams = [
                ABLTeamInfoSchema(
                    external_team_id=item.team_id,
                    team_name=item.team_name,
                    logo_url=item.team_logo,
                    league=LeagueTypeEnum.ABL,
                )
                for item in division_items
            ]
            div_first = division_items[0]
            div = ABLDivisionInfoSchema(
                external_division_id=division_id,
                name=div_first.division_name,
                teams=teams,
                league=LeagueTypeEnum.ABL,
            )
            divisions.append(div)
        league_seasons = [
            ABLLeagueSeasonInfoSchema(
                external_season_id=season_id_str,
                name=first.season_name,
            )
        ]
        season = ABLSeasonInfoSchema(
            name=first.season_name,
            start_year=first.season_start_year,
            end_year=first.season_end_year,
            divisions=divisions,
            league_seasons=league_seasons,
        )
        result.append(season)

    result.sort(key=lambda s: (s.start_year, s.end_year), reverse=True)
    return result


def match_bcl_season_info(seasons: tuple[BCLPlayerSeasonSchema, ...]) -> tuple[BCLSeasonInfoSchema, ...]:
    matched_seasons: dict[str, BCLSeasonInfoSchema] = {}
    for season in seasons:
        season_period, season_year = season.season_name.split(" ")
        season_year = int(season_year)
        start_year: int = season_year
        end_year: int = season_year
        season_period = season_period.lower()
        if season_period == BCL_AUTUMN_SEASON_NAME:
            start_year, end_year = season_year, season_year + 1
        elif season_period == BCL_SPRING_SEASON_NAME:
            start_year, end_year = season_year - 1, season_year
        season_name = SEASON_NAME_TEMPLATE.format(start_year=start_year, end_year=end_year)
        if season_info := matched_seasons.get(season_name):
            season_info.league_seasons.append(
                BCLLeagueSeasonInfoSchema(external_season_id=str(season.season_id), name=season.season_name)
            )
        else:
            matched_seasons[season_name] = BCLSeasonInfoSchema(
                name=season_name,
                start_year=start_year,
                end_year=end_year,
                league_seasons=[
                    BCLLeagueSeasonInfoSchema(external_season_id=str(season.season_id), name=season.season_name)
                ],
                divisions=[],
            )
    return tuple(matched_seasons.values())
