from typing import Final

from pydantic import AnyHttpUrl

from common.domain.dto import BaseSchema
from common.domain.dto.league_reader_input import LeagueTypeEnum
from src.constants import (
    ABL_FAST_STATISTICS_TUTORIAL,
    ABL_PLAYER_PROFILE_SCREENSHOT,
    BCL_FAST_STATISTICS_TUTORIAL,
    FAST_STATISTICS_TUTORIAL_0_STEP,
    FAST_STATISTICS_TUTORIAL_1_STEP,
    FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
    FAST_STATISTICS_TUTORIAL_2_STEP,
    FAST_STATISTICS_TUTORIAL_2_STEP_SCREENSHOT,
    MLBL_FAST_STATISTICS_TUTORIAL,
    MLBL_PLAYER_PROFILE_SCREENSHOT,
)
from src.constants.directories import BCL_PLAYER_PROFILE_SCREENSHOT


class ScreenshotSchema(BaseSchema):
    screenshot_path: str
    tutorial_caption: str


class UserTutorialSchema(BaseSchema):
    tutorial_text: str
    screenshots: tuple[ScreenshotSchema, ...]


class LeagueBaseSchema(BaseSchema):
    id: int
    name: str
    main_page_url: AnyHttpUrl
    player_profile_screenshot: str
    fast_statistic_tutorial: UserTutorialSchema


ID_GENERATOR = iter(range(10))

MLBL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    name=LeagueTypeEnum.MLBL.value,
    main_page_url=AnyHttpUrl("https://ilovebasket.ru/"),
    player_profile_screenshot=MLBL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistic_tutorial=UserTutorialSchema(
        tutorial_text=MLBL_FAST_STATISTICS_TUTORIAL,
        screenshots=(
            ScreenshotSchema(
                screenshot_path=MLBL_PLAYER_PROFILE_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_0_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
            ),
        ),
    ),
)
ABL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    name=LeagueTypeEnum.ABL.value,
    main_page_url=AnyHttpUrl("https://ablforpeople.com/"),
    player_profile_screenshot=ABL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistic_tutorial=UserTutorialSchema(
        tutorial_text=ABL_FAST_STATISTICS_TUTORIAL,
        screenshots=(
            ScreenshotSchema(
                screenshot_path=ABL_PLAYER_PROFILE_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_0_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
            ),
        ),
    ),
)
BCL: Final[LeagueBaseSchema] = LeagueBaseSchema(
    id=next(ID_GENERATOR),
    name=LeagueTypeEnum.BCL.value,
    main_page_url=AnyHttpUrl("https://basketball.businesschampions.ru/"),
    player_profile_screenshot=BCL_PLAYER_PROFILE_SCREENSHOT,
    fast_statistic_tutorial=UserTutorialSchema(
        tutorial_text=BCL_FAST_STATISTICS_TUTORIAL,
        screenshots=(
            ScreenshotSchema(
                screenshot_path=BCL_PLAYER_PROFILE_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_0_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
            ),
            ScreenshotSchema(
                screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_SCREENSHOT,
                tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
            ),
        ),
    ),
)
FAST_STATISTICS_DEFAULT_TUTORIAL_SCREENSHOTS: Final[tuple[ScreenshotSchema, ...]] = (
    ScreenshotSchema(
        screenshot_path=MLBL_PLAYER_PROFILE_SCREENSHOT,
        tutorial_caption=FAST_STATISTICS_TUTORIAL_0_STEP,
    ),
    ScreenshotSchema(
        screenshot_path=FAST_STATISTICS_TUTORIAL_1_STEP_SCREENSHOT,
        tutorial_caption=FAST_STATISTICS_TUTORIAL_1_STEP,
    ),
    ScreenshotSchema(
        screenshot_path=FAST_STATISTICS_TUTORIAL_2_STEP_SCREENSHOT,
        tutorial_caption=FAST_STATISTICS_TUTORIAL_2_STEP,
    ),
)


LEAGUES: Final[dict[int, LeagueBaseSchema]] = {MLBL.id: MLBL, ABL.id: ABL, BCL.id: BCL}
