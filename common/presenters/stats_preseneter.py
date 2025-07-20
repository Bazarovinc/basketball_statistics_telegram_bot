from abc import ABC, abstractmethod

from common.domain.dto import Schema


class PlayerStatisticsPresenter(ABC):
    @abstractmethod
    def present(self, input_data: type[Schema]) -> type[Schema]: ...
