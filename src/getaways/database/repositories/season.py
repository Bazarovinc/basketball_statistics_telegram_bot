from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import SeasonBaseSchema
from src.domain.dto.leagues_data.base import SeasonInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.season_repository import ISeasonRepository
from src.utils import async_serialize


class SeasonRepository(BaseRepository, ISeasonRepository):
    table_name = "season"
    schema: type[SeasonBaseSchema]

    @async_serialize
    async def upsert(self, data: SeasonInfoBaseSchema) -> SeasonBaseSchema:
        row = await self._connection.fetchrow(
            """
            INSERT INTO season (season_id, name, start_year, end_year, current_season)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT (start_year, end_year) DO UPDATE SET
                last_update_date = now(),
                current_season = EXCLUDED.current_season
            RETURNING season_id, name, current_season, start_year, end_year, create_date, last_update_date
            """,
            data.season_id,
            data.name,
            data.start_year,
            data.end_year,
            data.current_season,
        )
        return dict(row)
