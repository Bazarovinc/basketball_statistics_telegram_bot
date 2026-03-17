from src.core.domain.dto import BaseSchema, PlayerStatisticsPresenterBaseSchema


class FastStatisticsOutputSchema(BaseSchema):
    images: tuple[tuple[bytes, str], ...]
    fast_statistics: PlayerStatisticsPresenterBaseSchema
