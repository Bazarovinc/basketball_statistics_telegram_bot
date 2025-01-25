from typing import Final

# MLBL
MLBL_PLAYER_PROFILE_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/PlayerPage/{player_id}?format=json"
)
MLBL_PLAYER_STATS_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/PlayerStats/{player_id}?compId={comp_id}&"
    "filter=1&format=json&team=0"
)
MLBL_PLAYER_TEAM_INFO_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/TeamRoster/{team_id}?compId={comp_id}&format=json&lang=ru"
)
MLBL_TEAM_GAMES_CALENDAR_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/TeamGames/{team_id}?compId={comp_id}&format=json"
)
MLBL_GAME_STATISTIC_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/GetOnline/{game_id}?format=json&lang=ru"
)
MLBL_TEAM_LOGO_ADDRESS: Final[str] = (
    "https://reg.infobasket.su/Widget/GetTeamLogo/{team_id}?compId={comp_id}"
)

MLBL_HOST: Final[str] = ".ilovebasket.ru"
MLBL_PLAYER_PATH_PARAM: Final[str] = "players"
MLBL_TEAM_PATH_PARAM: Final[str] = "teams"

# ABL
ABL_HOST: Final[str] = "ablforpeople.com"
ABL_PLAYER_PATH_PARAM: Final[str] = "player"
ABL_PLAYER_PROFILE_ADDRESS: Final[str] = "https://mtgame.ru/api/v1/league_player/{player_id}/"
ABL_PLAYED_GAMES_ADDRESS: Final[str] = (
    "https://mtgame.ru/api/v1/tournament_season/{season_id}/games/"
    "?page=1&size=999&league_player_id={player_id}"
)
ABL_GAME_USERS_ADDRESS: Final[str] = "https://mtgame.ru/api/v1/tournament_game/{game_id}/users/"
ABL_GAME_USERS_STATISTICS_ADDRESS: Final[str] = (
    "https://mtgame.ru/api/v1/tournament_basketball_game/{game_id}/user_statistic/"
)

# BCL
BCL_HOST: Final[str] = "basketball.businesschampions.ru"
