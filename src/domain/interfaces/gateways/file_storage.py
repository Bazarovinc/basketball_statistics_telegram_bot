from abc import ABC, abstractmethod
from io import BytesIO


class FileStorage(ABC):
    @abstractmethod
    async def save_file(self, file: BytesIO, file_key: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_file(self, file_key: str) -> BytesIO:
        raise NotImplementedError

    @abstractmethod
    async def delete_file(self, file_key: str) -> None:
        raise NotImplementedError
