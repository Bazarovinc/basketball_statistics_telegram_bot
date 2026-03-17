from dependency_injector import containers, providers

from src.containers.getaways import GetawaysContainer
from src.containers.presenters import PresentersContainer
from src.containers.repos import ReposContainer
from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.use_cases.core_use_cases.fast_statistics import FastStatisticsGetter
from src.domain.use_cases.core_use_cases.full_statistics_saver import FullStatisticsSaver
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService
from src.domain.use_cases.core_use_cases.user_service import UserService
from src.domain.use_cases.parsers.abl_parser import ABLParser
from src.domain.use_cases.parsers.bcl_parser import BCLParser
from src.domain.use_cases.parsers.factory import ParserFactory
from src.domain.use_cases.parsers.mlbl_parser import MLBLParser
from src.settings import app_settings


class UseCasesContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.controllers.telegram_bot"])
    repos: ReposContainer = providers.Container(ReposContainer, config=app_settings.postgres)
    presenters: PresentersContainer = providers.Container(PresentersContainer)
    getaways: GetawaysContainer = providers.Container(GetawaysContainer)
    leagues_service = providers.Singleton(LeaguesService, leagues_info_presenter=presenters.leagues_info_presenter)
    parser_factory = providers.Factory(
        ParserFactory,
        parsers=providers.Dict(
            {
                LeagueTypeEnum.ABL: providers.Factory(ABLParser, league_reader=getaways.league_reader),
                LeagueTypeEnum.BCL: providers.Factory(BCLParser, league_reader=getaways.league_reader),
                LeagueTypeEnum.MLBL: providers.Factory(MLBLParser, league_reader=getaways.league_reader),
            }
        ),
    )
    fast_statistics_getter = providers.Factory(
        FastStatisticsGetter, parser_factory=parser_factory, presenter=presenters.graphics_presenter
    )
    full_statistics_saver = providers.Factory(
        FullStatisticsSaver,
        parser_factory=parser_factory,
        uow=repos.full_statistics_saver_uow,
        file_storage=getaways.object_storage_client,
        image_loader=getaways.image_loader,
    )
    user_service = providers.Factory(UserService, uow=repos.user_service_uow)
