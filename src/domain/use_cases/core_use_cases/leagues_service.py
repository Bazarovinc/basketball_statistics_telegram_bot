from loguru import logger

from src.domain.dto.base.league import LeagueBaseSchema, ScreenshotSchema
from src.presenters.interfaces import LeagueInfoPresenterInterface


class LeaguesService:

    def __init__(self, leagues_info_presenter: LeagueInfoPresenterInterface):
        self._leagues_info_presenter = leagues_info_presenter

    def get_all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        return self._leagues_info_presenter.all_leagues

    def get_league_by_id(self, league_id: str) -> LeagueBaseSchema:
        logger.info(f"Получение лиги с id={league_id}")
        return self._leagues_info_presenter.get_league_by_id(int(league_id.split("_")[-1]))

    def get_default_tutorial(self) -> tuple[ScreenshotSchema, ...]:
        return self._leagues_info_presenter.default_tutorial
