import asyncio

from loguru import logger
from pydantic import AnyHttpUrl

from common.exceptions.parsers_exceptions import ServerNotAvailableException
from src.constants import MLBL_PLAYER_PROFILE_ADDRESS, MLBL_PLAYER_STATS_ADDRESS
from src.domain.dto.leagues_data.mlbl.fast_statistics import MLBLUserStatsPerGameResponseSchema
from src.domain.dto.leagues_data.mlbl.reader_input import MLBLInputBaseSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class MLBLParser(LeagueParser[MLBLInputBaseSchema]):
    input_schema = MLBLInputBaseSchema

    player_profile_address: str | AnyHttpUrl = MLBL_PLAYER_PROFILE_ADDRESS
    player_stats_address: str | AnyHttpUrl = MLBL_PLAYER_STATS_ADDRESS
    # player_team_info_address: str | AnyHttpUrl = PLAYER_TEAM_INFO_ADDRESS
    # team_games_calendar_address: str | AnyHttpUrl = TEAM_GAMES_CALENDAR_ADDRESS
    # game_statistic_address: str | AnyHttpUrl = GAME_STATISTIC_ADDRESS
    # team_logo_address: str | AnyHttpUrl = TEAM_LOGO_ADDRESS

    # async def _get_statistic_for_finished_games(
    #     self, games: list[MLBLGameResponseSchema]
    # ) -> list[MLBLGameStatisticResponseSchema]:
    #     games_requests = [
    #         asyncio.ensure_future(
    #             self._league_reader.get_data(
    #                 self.game_statistic_address.format(game_id=game.game_id)
    #             )
    #         )
    #         for game in games
    #         if game.game_status is MLBLGameStatusEnum.finished
    #     ]
    #     return TypeAdapter(list[MLBLGameStatisticResponseSchema]).validate_python(
    #         (await asyncio.gather(*games_requests))
    #     )
    #

    def _set_player_addresses_variables(self, data_from_user: MLBLInputBaseSchema) -> None:
        logger.info("Формирование URL-адресов для получения данных по игроку")
        self.player_profile_address = AnyHttpUrl(self.player_profile_address.format(player_id=data_from_user.player_id))
        self.player_stats_address = AnyHttpUrl(
            self.player_stats_address.format(player_id=data_from_user.player_id, comp_id=data_from_user.player_comp_id)
        )

    # def _set_team_addresses_variables(self, data_from_user: MLBLInputBaseSchema) -> None:
    #     self.player_team_info_address = AnyHttpUrl(
    #         self.player_team_info_address.format(
    #             team_id=data_from_user.team_id, comp_id=data_from_user.team_comp_id
    #         )
    #     )
    #     self.team_games_calendar_address = AnyHttpUrl(
    #         self.team_games_calendar_address.format(
    #             team_id=data_from_user.team_id, comp_id=data_from_user.team_comp_id
    #         )
    #     )
    #     self.team_logo_address = AnyHttpUrl(
    #         self.team_logo_address.format(
    #             team_id=data_from_user.team_id, comp_id=data_from_user.team_comp_id
    #         )
    #     )

    # def _set_addresses_variables(self, data_from_user: MLBLInputBaseSchema) -> None:
    #     if not (data_from_user.team_id and data_from_user.team_comp_id):
    #         # TODO: ошибку
    #         raise
    #     self._set_player_addresses_variables(data_from_user)
    #     self._set_team_addresses_variables(data_from_user)

    #
    # async def _get_images(self, images_addresses: list[AnyHttpUrl]) -> tuple[bytes]:
    #     if len(images_addresses) == 1:
    #         return ((await self._league_reader.get_image(images_addresses[0].unicode_string())),)
    #     images_requests = [
    #         asyncio.ensure_future(self._league_reader.get_image(image_address))
    #         for image_address in images_addresses
    #     ]
    #     return await asyncio.gather(*images_requests)
    #
    # async def parse_player_info_and_statistic(self, data_from_user: MLBLInputSchema): ...
    #
    # async def parse_full_player_info(self, data_from_user: MLBLInputBaseSchema) -> tuple[
    #     MLBLPlayerProfileResponseSchema,
    #     MLBLTeamResponseSchema,
    #     list[MLBLGameResponseSchema],
    #     list[MLBLGameStatisticResponseSchema],
    # ]:
    #     self._set_addresses_variables(data_from_user)
    #     player_profile_response, team_profile_response, games_calendar_response = (
    #         await asyncio.gather(
    #             *[
    #                 asyncio.ensure_future(
    #                     self._league_reader.get_data(self.player_profile_address.unicode_string())
    #                 ),
    #                 asyncio.ensure_future(
    #                     self._league_reader.get_data(self.player_team_info_address.unicode_string())
    #                 ),
    #                 asyncio.ensure_future(
    #                     self._league_reader.get_data(
    #                         self.team_games_calendar_address.unicode_string()
    #                     )
    #                 ),
    #             ]
    #         )
    #     )
    #     games_calendar = TypeAdapter(list[MLBLGameResponseSchema]).validate_python(
    #         games_calendar_response
    #     )
    #     games_statistic = await self._get_statistic_for_finished_games(games_calendar)
    #     return (
    #         MLBLPlayerProfileResponseSchema(**player_profile_response),
    #         MLBLTeamResponseSchema(**team_profile_response),
    #         games_calendar,
    #         games_statistic,
    #     )

    async def parse_fast_statistic(self, data_from_user: MLBLInputBaseSchema) -> MLBLUserStatsPerGameResponseSchema:
        data_from_user = self._validate_input(data_from_user)
        logger.info("Получение данных из лиги МЛБЛ для быстрой статистики")
        self._set_player_addresses_variables(data_from_user)
        player_info, statistics = await asyncio.gather(
            *(
                self._league_reader.get_data_json(self.player_profile_address.unicode_string()),
                self._league_reader.get_data_json(self.player_stats_address.unicode_string()),
            )
        )
        if not all((player_info, statistics)):
            logger.error("Данный от лиги не получены")
            raise ServerNotAvailableException()
        statistics["player_info"] = player_info
        return MLBLUserStatsPerGameResponseSchema(**statistics)
