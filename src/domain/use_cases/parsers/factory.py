from typing import Type

from loguru import logger
from pydantic import ValidationError

from common.domain.dto.league_reader_input import LeagueReaderInputSchema
from common.domain.dto.statistics_presenter import PlayerStaticsPresenterSchema
from common.exceptions.parsers_exceptions import URLValidationException
from src.constants import (
    ABL_FAST_STATISTICS_TUTORIAL,
    ABL_HOST,
    BCL_FAST_STATISTICS_TUTORIAL,
    BCL_HOST,
    MLBL_FAST_STATISTICS_TUTORIAL,
    MLBL_HOST,
)
from src.domain.dto.leagues_data.abl.reader_input import ABLInputBaseSchema
from src.domain.dto.leagues_data.bcl.reader_input import BCLInputBaseSchema
from src.domain.dto.leagues_data.mlbl.reader_input import MLBLInputBaseSchema
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class ParserFactory:

    def __init__(
        self, mlbl_parser: LeagueParser, bcl_parser: LeagueParser, abl_parser: LeagueParser
    ) -> None:
        self._mlbl_parser = mlbl_parser
        self._bcl_parser = bcl_parser
        self._abl_parser = abl_parser
        self.parser: LeagueParser | None = None
        self.schema: Type[LeagueReaderInputSchema] | None = None

    def _set_parser(self, data_from_user: LeagueUrlsUserInputSchema) -> None:
        logger.info("Выбор парсера по ссылке присланной пользователем")
        if (
            MLBL_HOST in data_from_user.player_url.host
            and data_from_user.reply_message_text == MLBL_FAST_STATISTICS_TUTORIAL
        ):
            logger.info("Пользователь прислал ссылку для лиги МЛБЛ")
            self.parser = self._mlbl_parser
            self.schema = MLBLInputBaseSchema
        elif (
            ABL_HOST in data_from_user.player_url.host
            and data_from_user.reply_message_text == ABL_FAST_STATISTICS_TUTORIAL
        ):
            self.parser = self._abl_parser
            self.schema = ABLInputBaseSchema
        elif (
            BCL_HOST == data_from_user.player_url.host
            and data_from_user.reply_message_text == BCL_FAST_STATISTICS_TUTORIAL
        ):
            logger.info("Пользователь прислал ссылку для лиги ЛЧБ")
            self.parser = self._bcl_parser
            self.schema = BCLInputBaseSchema
        else:
            raise URLValidationException()

    async def parse_fast_statistic(
        self, data_from_user: LeagueUrlsUserInputSchema
    ) -> PlayerStaticsPresenterSchema:

        self._set_parser(data_from_user)
        try:
            data = self.schema(**data_from_user.model_dump())
        except ValidationError as error:
            logger.error(error)
            raise URLValidationException()
        return await self.parser.parse_fast_statistic(data)
