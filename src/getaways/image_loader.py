from httpx import AsyncClient, AsyncHTTPTransport, codes
from loguru import logger

from src.domain.interfaces.gateways.image_loader import ImageLoader


class ImageLoaderClient(ImageLoader):
    def __init__(self, retries: int = 3) -> None:
        self._retries = retries

    async def load(self, url: str) -> bytes | None:
        transport = AsyncHTTPTransport(retries=self._retries)
        async with AsyncClient(transport=transport) as http_client:
            response = await http_client.get(url)
            if response.status_code == codes.OK:
                return response.content
            logger.error("Не удалось загрузить изображение: {} (status={})", url, response.status_code)
            return None
