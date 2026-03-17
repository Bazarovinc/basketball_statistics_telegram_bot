from abc import ABC, abstractmethod


class ImageLoader(ABC):
    @abstractmethod
    async def load(self, url: str) -> bytes | None:
        """Загружает изображение по URL и возвращает байты содержимого или None при ошибке."""
        raise NotImplementedError
