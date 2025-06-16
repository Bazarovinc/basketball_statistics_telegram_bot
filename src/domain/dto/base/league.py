from typing import Final

from pydantic import AnyHttpUrl

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum
from src.constants import (
    ABL_HOST,
    ABL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
    ABL_PLAYER_PROFILE_SCREENSHOT,
    BCL_HOST,
    BCL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
    BCL_PLAYER_PROFILE_SCREENSHOT,
    FAST_STATISTICS_REPLY_MESSAGE,
    FAST_STATISTICS_TUTORIAL_1_STEP,
    FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_2_STEP,
    FAST_STATISTICS_TUTORIAL_2_STEP_ABL_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_2_STEP_BCL_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_2_STEP_MLBL_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_3_STEP,
    FAST_STATISTICS_TUTORIAL_4_STEP,
    FAST_STATISTICS_TUTORIAL_4_STEP_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_5_STEP,
    FAST_STATISTICS_TUTORIAL_5_STEP_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_MESSAGE,
    MLBL_HOST,
    MLBL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
    MLBL_PLAYER_PROFILE_SCREENSHOT,
)


class ScreenshotSchema(BaseSchema):
    screenshot_path: str
    tutorial_caption: str


class UserTutorialSchema(BaseSchema):
    tutorial_text: str
    screenshots: tuple[ScreenshotSchema, ...]


class FastStatisticsInfoSchema(BaseSchema):
    tutorial: UserTutorialSchema
    reply_message: str
    profile_link: AnyHttpUrl


class LeagueBaseSchema(BaseSchema):
    id: int
    league_type: LeagueTypeEnum
    main_page_url: AnyHttpUrl
    host: str
    player_profile_screenshot: str
    fast_statistics_info: FastStatisticsInfoSchema

    @property
    def name(self) -> str:
        return self.league_type.value


ID_GENERATOR = iter(range(10))

MLBL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    league_type=LeagueTypeEnum.MLBL,
    main_page_url=AnyHttpUrl("https://ilovebasket.ru/"),
    host=MLBL_HOST,
    player_profile_screenshot=MLBL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistics_info=FastStatisticsInfoSchema(
        profile_link=MLBL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
        reply_message=FAST_STATISTICS_REPLY_MESSAGE.format(link=MLBL_PLAYER_PROFILE_EXAMPLE_ADDRESS),
        tutorial=UserTutorialSchema(
            tutorial_text=FAST_STATISTICS_TUTORIAL_MESSAGE,
            screenshots=(
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_MLBL_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=MLBL_PLAYER_PROFILE_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_3_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_4_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_4_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_5_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_5_STEP,
                ),
            ),
        ),
    ),
)
ABL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    league_type=LeagueTypeEnum.ABL,
    main_page_url=AnyHttpUrl("https://ablforpeople.com/"),
    host=ABL_HOST,
    player_profile_screenshot=ABL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistics_info=FastStatisticsInfoSchema(
        profile_link=ABL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
        reply_message=FAST_STATISTICS_REPLY_MESSAGE.format(link=ABL_PLAYER_PROFILE_EXAMPLE_ADDRESS),
        tutorial=UserTutorialSchema(
            tutorial_text=FAST_STATISTICS_TUTORIAL_MESSAGE,
            screenshots=(
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_ABL_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=ABL_PLAYER_PROFILE_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_3_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_4_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_4_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_5_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_5_STEP,
                ),
            ),
        ),
    ),
)
BCL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    league_type=LeagueTypeEnum.BCL,
    main_page_url=AnyHttpUrl("https://basketball.businesschampions.ru/"),
    host=BCL_HOST,
    player_profile_screenshot=BCL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistics_info=FastStatisticsInfoSchema(
        profile_link=BCL_PLAYER_PROFILE_EXAMPLE_ADDRESS,
        reply_message=FAST_STATISTICS_REPLY_MESSAGE.format(link=BCL_PLAYER_PROFILE_EXAMPLE_ADDRESS),
        tutorial=UserTutorialSchema(
            tutorial_text=FAST_STATISTICS_TUTORIAL_MESSAGE,
            screenshots=(
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_BCL_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=BCL_PLAYER_PROFILE_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_3_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_4_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_4_STEP,
                ),
                ScreenshotSchema(
                    screenshot_path=FAST_STATISTICS_TUTORIAL_5_STEP_SCREENSHOT,
                    tutorial_caption=FAST_STATISTICS_TUTORIAL_5_STEP,
                ),
            ),
        ),
    ),
)


LEAGUES: Final[dict[int, LeagueBaseSchema]] = {MLBL.id: MLBL, ABL.id: ABL, BCL.id: BCL}
