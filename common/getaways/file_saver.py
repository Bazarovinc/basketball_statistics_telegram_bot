from abc import ABC, abstractmethod
from pathlib import Path


class FileSaver(ABC):

    @abstractmethod
    def save(self, filepath: Path, filename: str, file: bytes, extension: str = "jpg") -> str:
        raise NotImplementedError
