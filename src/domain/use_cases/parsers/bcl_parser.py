from bs4 import BeautifulSoup
from loguru import logger

from common.exceptions.parsers_exceptions import ServerNotAvailableException
from src.domain.dto.leagues_data.bcl.fast_statistics import (
    BCLFastStatisticsSchema,
    BCLPlayerFastStatisticsResponseSchema,
)
from src.domain.dto.leagues_data.bcl.reader_input import BCLInputBaseSchema
from src.domain.use_cases.parsers.interface import LeagueParser


class BCLParser(LeagueParser[BCLInputBaseSchema]):
    input_schema = BCLInputBaseSchema

    async def get_fast_statistics(self, data_from_user: BCLInputBaseSchema) -> BCLFastStatisticsSchema:
        data_from_user = self._validate_input(data_from_user)
        html = await self._league_reader.get_data_html(data_from_user.player_url.unicode_string())
        if not html:
            logger.error("Данный от лиги не получены")
            raise ServerNotAvailableException()
        soup = BeautifulSoup(html, "html.parser")
        sections = soup.findAll("section")
        game_statistics: list[dict] = []
        player_info: BCLPlayerFastStatisticsResponseSchema | None = None
        games_count: int = 0
        for i, section in enumerate(sections):
            header = section.find("header")
            if header and i == 1:
                last_name, first_name = header.text.split()
                player_info = BCLPlayerFastStatisticsResponseSchema(last_name=last_name, first_name=first_name)
            if header and header.text == "Статистика":
                table = section.find("table")
                names = (th.text for th in table.find("thead").find_all("th"))
                values = (td.text for td in table.find("tbody").find_all("td"))
                stats = {key: value for key, value in zip(names, values)}
                games_count = int(stats.get("Игр"))
            if header and header.text == "Матчи":
                table = section.find("table")
                names = ((th.text for th in table.find("thead").find_all("th")) for _ in range(games_count))
                values = (td.text for td in table.find("tbody").find_all("td"))
                game_statistics = [{key: value for key, value in zip(i, values)} for i in names]
        return BCLFastStatisticsSchema(player_info=player_info, statistics_per_game=game_statistics)
