from dependency_injector import containers, providers

from src.presenters.leagues_info_presenter import LeagueInfoPresenter
from src.presenters.matplotlib_graphic_presenter import MatplotlibGraphicsPresenter


class PresentersContainer(containers.DeclarativeContainer):
    leagues_info_presenter = providers.Singleton(LeagueInfoPresenter)
    graphics_presenter = providers.Singleton(MatplotlibGraphicsPresenter)
