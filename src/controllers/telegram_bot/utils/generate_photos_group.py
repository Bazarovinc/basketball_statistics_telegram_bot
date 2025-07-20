from telegram import InputMediaPhoto

from src.domain.dto.base.league import ScreenshotSchema


def generate_tutorial_photos_group(
    images: tuple[ScreenshotSchema, ...],
) -> tuple[InputMediaPhoto, ...]:
    return tuple(
        InputMediaPhoto(open(screenshot.screenshot_path, "rb"), caption=screenshot.tutorial_caption)
        for screenshot in images
    )
