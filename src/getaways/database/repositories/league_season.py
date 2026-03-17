import uuid

from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import LeagueSeasonBaseSchema
from src.domain.dto.leagues_data.base import LeagueSeasonInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.league_season_repository import ILeagueSeasonRepository
from src.utils import async_serialize


class LeagueSeasonRepository(BaseRepository, ILeagueSeasonRepository):
    table_name = "league_season"
    schema: type[LeagueSeasonBaseSchema]

    @async_serialize
    async def upsert(self, season_id: uuid.UUID, data: LeagueSeasonInfoBaseSchema) -> None:
        await self._connection.execute(
            """
            INSERT INTO league_season (league_season_id, season_id, external_season_id, name, league)
            VALUES ($1, $2, $3, $4, $5::league_enum)
            ON CONFLICT (external_season_id, league) DO UPDATE SET
                name = EXCLUDED.name,
                last_update_date = now()
            """,
            data.league_season_id,
            season_id,
            data.external_season_id,
            data.name,
            data.league,
        )
