from pydantic import AnyHttpUrl

from common.domain.dto import BaseSchema


class LeagueUrlsUserInputSchema(BaseSchema):
    reply_message_text: str
    player_url: AnyHttpUrl
    team_url: AnyHttpUrl | None = None
