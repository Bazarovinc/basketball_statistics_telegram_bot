from common.domain.dto import BaseSchema
from common.domain.dto.statistics_presenter import PlayerStatisticsPresenterBaseSchema


class FastStatisticsOutputSchema(BaseSchema):
    images: tuple[tuple[bytes, str], ...]
    fast_statistics: PlayerStatisticsPresenterBaseSchema
