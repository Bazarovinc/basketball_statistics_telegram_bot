from src.domain.interfaces.gateways.database.unit_of_work import FullStatisticsSaverBaseUnitOfWork
from src.getaways.database.repositories import (
    DivisionRepository,
    GameRepository,
    LeagueSeasonRepository,
    PlayerGameStatisticsRepository,
    PlayerProfileRepository,
    PlayerTeamRepository,
    SeasonRepository,
    TeamDivisionRepository,
    TeamRepository,
    UserAgreementRepository,
    UserRepository,
)


class FullStatisticsSaverUnitOfWork(FullStatisticsSaverBaseUnitOfWork):
    user_repo: UserRepository
    user_agreement_repo: UserAgreementRepository
    division_repo: DivisionRepository
    season_repo: SeasonRepository
    league_season_repo: LeagueSeasonRepository
    game_repo: GameRepository
    team_division_repo: TeamDivisionRepository
    team_repo: TeamRepository
    player_game_statistics_repo: PlayerGameStatisticsRepository
    player_team_repo: PlayerTeamRepository
    player_profile_repo: PlayerProfileRepository
