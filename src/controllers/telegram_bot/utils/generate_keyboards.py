from typing import Sequence

from loguru import logger
from telegram import InlineKeyboardButton

from src.constants import CANCEL_BUTTON, CANCEL_BUTTON_CALLBACK
from src.domain.dto.base.league import LeagueBaseSchema


def generate_leagues_keyboard(
    leagues: Sequence[LeagueBaseSchema], callback_template: str
) -> list[tuple[InlineKeyboardButton]]:
    logger.info("Генерация кнопок выбора лиг")
    return [
        (InlineKeyboardButton(league.name, callback_data=callback_template + str(league.id)),)
        for league in leagues
    ]


def generate_cancel_button(text: str = CANCEL_BUTTON) -> list[tuple[InlineKeyboardButton]]:
    logger.info(f"Генерация кнопки {text}")
    return [(InlineKeyboardButton(text=text, callback_data=CANCEL_BUTTON_CALLBACK),)]
