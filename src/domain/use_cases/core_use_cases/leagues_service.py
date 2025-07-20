from loguru import logger

from common.domain.dto.league_reader_input import LeagueTypeEnum
from src.domain.dto.base.league import LeagueBaseSchema
from src.presenters.interfaces import LeagueInfoPresenterInterface


class LeaguesService:
    def __init__(self, leagues_info_presenter: LeagueInfoPresenterInterface) -> None:
        self._leagues_info_presenter = leagues_info_presenter

    def get_all_leagues(self) -> tuple[LeagueBaseSchema, ...]:
        return self._leagues_info_presenter.all_leagues

    def get_league_by_id(self, league_id: str) -> LeagueBaseSchema:
        logger.info(f"Получение лиги с id={league_id}")
        return self._leagues_info_presenter.get_league_by_id(int(league_id.split("_")[-1]))

    def get_league_type_by_fast_statistics(self, text: str) -> LeagueTypeEnum | None:
        return self._leagues_info_presenter.get_league_type_by_fast_statistics(text)
