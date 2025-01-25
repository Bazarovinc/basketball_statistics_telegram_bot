from dependency_injector import containers, providers

from src.containers.getaways import GetawaysContainer
from src.containers.presenters import PresentersContainer
from src.domain.use_cases.core_use_cases.fast_statistics import FastStatisticsGetter
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService
from src.domain.use_cases.parsers.abl_parser import ABLParser
from src.domain.use_cases.parsers.bcl_parser import BCLParser
from src.domain.use_cases.parsers.factory import ParserFactory
from src.domain.use_cases.parsers.mlbl_parser import MLBLParser


class UseCasesContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.controllers.telegram_bot"])
    presenters = providers.Container(PresentersContainer)
    getaways = providers.Container(GetawaysContainer)
    leagues_service = providers.Singleton(
        LeaguesService, leagues_info_presenter=presenters.leagues_info_presenter
    )
    mlbl_parser = providers.Factory(MLBLParser, league_reader=getaways.league_reader)
    bcl_parser = providers.Factory(BCLParser, league_reader=getaways.league_reader)
    abl_parser = providers.Factory(ABLParser, league_reader=getaways.league_reader)
    parser_factory = providers.Factory(
        ParserFactory, mlbl_parser=mlbl_parser, bcl_parser=bcl_parser, abl_parser=abl_parser
    )
    fast_statistics_getter = providers.Factory(
        FastStatisticsGetter, parser_factory=parser_factory, presenter=presenters.graphics_presenter
    )
