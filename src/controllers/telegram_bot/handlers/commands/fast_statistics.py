from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.constants import FAST_STATISTICS_MESSAGE, USER_COMMAND_CALL
from src.constants.templates import FAST_STATISTICS_LEAGUE_BUTTON_TEMPLATE
from src.containers.use_cases import UseCasesContainer
from src.controllers.telegram_bot.states import START_ROUTES
from src.controllers.telegram_bot.utils.generate_keyboards import (
    generate_cancel_button,
    generate_leagues_keyboard,
)
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_fast_statistics_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    logger.info(
        USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id)
    )
    await update.message.reply_text(
        FAST_STATISTICS_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            generate_leagues_keyboard(
                use_case.get_all_leagues(), FAST_STATISTICS_LEAGUE_BUTTON_TEMPLATE
            )
            + generate_cancel_button(),
        ),
    )
    return START_ROUTES
