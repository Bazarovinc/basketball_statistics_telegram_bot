from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.constants import (
    FAST_STATISTICS_LEAGUE_TUTORIAL_BUTTON_TEMPLATE,
    FAST_STATISTICS_TUTORIAL_COMMAND_MESSAGE,
    USER_COMMAND_CALL,
)
from src.containers.use_cases import UseCasesContainer
from src.controllers.telegram_bot.states import TUTORIAL_START_ROUTES
from src.controllers.telegram_bot.utils import generate_cancel_button, generate_leagues_keyboard
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_fast_statistic_tutorial_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    logger.info(
        USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id)
    )
    await update.message.reply_text(
        FAST_STATISTICS_TUTORIAL_COMMAND_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            generate_leagues_keyboard(
                use_case.get_all_leagues(), FAST_STATISTICS_LEAGUE_TUTORIAL_BUTTON_TEMPLATE
            )
            + generate_cancel_button(),
        ),
    )
    return TUTORIAL_START_ROUTES
