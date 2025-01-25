from httpx import AsyncClient, AsyncHTTPTransport
from loguru import logger

from common.getaways.league_reader import LeagueReaderInterface


class LeagueReader(LeagueReaderInterface):
    def __init__(self):
        self._retries = 3

    async def get_data_json(self, address: str) -> dict | None:
        logger.info("Получение данных")
        retry_strategy = AsyncHTTPTransport(retries=self._retries)
        async with AsyncClient(transport=retry_strategy) as http_client:
            response = await http_client.get(address)
            if response.status_code == 200:
                logger.info("Данные успешно получены")
                return response.json()
            else:
                logger.error("Данные не получены")
                logger.critical(response.json())
                return None

    async def get_data_html(self, address: str) -> str | None:
        logger.info("Получение данных")
        retry_strategy = AsyncHTTPTransport(retries=self._retries)
        async with AsyncClient(transport=retry_strategy) as http_client:
            response = await http_client.get(address)
            if response.status_code == 200:
                logger.info("Данные успешно получены")
                return response.text
            else:
                logger.error("Данные не получены")
                logger.critical(response.text)
                return None

    # async def get_image(self, image_path: str) -> bytes | None:
    #     retry_strategy = AsyncHTTPTransport(retries=self._retries)
    #     async with AsyncClient(transport=retry_strategy) as http_client:
    #         response = await http_client.get(image_path)
    #         if response.status_code == 200:
    #             return response.content
    #         else:
    #             logger.error("Данные не получены")
    #             logger.critical(response.json())
    #             return None
