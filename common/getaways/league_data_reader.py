from abc import ABC, abstractmethod


class LeagueDataReader(ABC):

    @abstractmethod
    async def get_player_profile(self, address: str) -> dict: ...

    @abstractmethod
    async def get_player_games_statistics(self, address: str) -> dict: ...

    @abstractmethod
    async def get_player_team_info(self, address: str) -> dict: ...
