from src.core.gateways.database.unit_of_work.base import BaseUnitOfWork
from src.domain.interfaces.gateways.database.repositories import (
    IDivisionRepository,
    IGameRepository,
    ILeagueSeasonRepository,
    IPlayerGameStatisticsRepository,
    IPlayerProfileRepository,
    IPlayerTeamRepository,
    ISeasonRepository,
    ITeamDivisionRepository,
    ITeamRepository,
    IUserAgreementRepository,
    IUserRepository,
)


class FullStatisticsSaverBaseUnitOfWork(BaseUnitOfWork):
    user_repo: IUserRepository
    user_agreement_repo: IUserAgreementRepository
    division_repo: IDivisionRepository
    season_repo: ISeasonRepository
    league_season_repo: ILeagueSeasonRepository
    game_repo: IGameRepository
    team_division_repo: ITeamDivisionRepository
    team_repo: ITeamRepository
    player_game_statistics_repo: IPlayerGameStatisticsRepository
    player_team_repo: IPlayerTeamRepository
    player_profile_repo: IPlayerProfileRepository
