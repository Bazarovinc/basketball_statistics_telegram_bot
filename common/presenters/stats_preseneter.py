from abc import ABC, abstractmethod
from typing import Type

from common.domain.dto import Schema


class PlayerStatisticsPresenter(ABC):

    @abstractmethod
    def present(self, input_data: Type[Schema]) -> Type[Schema]:
        ...
