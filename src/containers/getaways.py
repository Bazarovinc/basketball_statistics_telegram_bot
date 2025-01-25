from dependency_injector import containers, providers

from src.getaways.league_reader import LeagueReader


class GetawaysContainer(containers.DeclarativeContainer):
    league_reader = providers.Singleton(LeagueReader)
