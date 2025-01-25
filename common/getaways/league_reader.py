from abc import ABC, abstractmethod


class LeagueReaderInterface(ABC):

    @abstractmethod
    async def get_data_json(self, address: str) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    async def get_data_html(self, address: str) -> str | None:
        raise NotImplementedError

    # @abstractmethod
    # async def get_image(self, image_path: str) -> bytes | None:
    #     raise NotImplementedError
