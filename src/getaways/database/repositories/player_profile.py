import uuid

import asyncpg

from src.core.domain.dto.league_reader_input import LeagueTypeEnum
from src.core.exceptions.repo_exceptions import DuplicatedRecordException
from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import PlayerProfileBaseSchema
from src.domain.dto.leagues_data.base import PlayerProfileInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.player_profile_repository import IPlayerProfileRepository


class PlayerProfileRepository(BaseRepository, IPlayerProfileRepository):
    table_name = "player_profile"
    schema: type[PlayerProfileBaseSchema]

    async def create(self, data: PlayerProfileInfoBaseSchema, user_id: uuid.UUID) -> None:
        try:
            await self._connection.execute(
                """
            INSERT INTO player_profile (
                player_profile_id, user_id, profile_id, first_name, last_name, middle_name,
                player_height, player_weight, birthdate, position, player_rank, photo,
                player_number, league, parse_date
            )
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14::league_enum, $15)
            """,
                data.player_profile_id,
                user_id,
                data.profile_id,
                data.first_name,
                data.last_name,
                data.middle_name,
                data.player_height,
                data.player_weight,
                data.birthdate,
                data.position,
                data.player_rank,
                str(data.photo) if data.photo else None,
                data.player_number,
                data.league,
                data.parse_date,
            )
        except asyncpg.exceptions.UniqueViolationError as error:
            raise DuplicatedRecordException from error

    async def is_exists(self, user_id: uuid.UUID, league: LeagueTypeEnum) -> bool:
        row = await self._connection.fetchrow(
            """
            SELECT EXISTS(
                SELECT 1 FROM player_profile
                WHERE user_id = $1 AND league = $2::league_enum
            ) AS "exists"
            """,
            user_id,
            league,
        )
        return row["exists"] if row else False
