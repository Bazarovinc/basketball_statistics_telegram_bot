from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import ADD_PROFILE_MESSAGE, PARSE_MODE, USER_AGREEMENT_NOT_FOUND_MESSAGE, USER_COMMAND_CALL
from src.constants.templates import ADD_PROFILE_LEAGUE_BUTTON_TEMPLATE
from src.containers.app import UseCasesContainer
from src.controllers.telegram_bot.states import ADD_PROFILE_START_ROUTES
from src.controllers.telegram_bot.utils.generate_keyboards import generate_cancel_button, generate_leagues_keyboard
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService
from src.domain.use_cases.core_use_cases.user_service import UserService


@inject
async def get_add_profile_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
    use_case: LeaguesService = Provide[UseCasesContainer.leagues_service],
    user_service: UserService = Provide[UseCasesContainer.user_service],
) -> int:
    logger.info(USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id))
    if not await user_service.check_user_agreement_exists(update.effective_user.id):
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=USER_AGREEMENT_NOT_FOUND_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    await update.message.reply_text(
        ADD_PROFILE_MESSAGE,
        parse_mode=PARSE_MODE,
        reply_markup=InlineKeyboardMarkup(
            generate_leagues_keyboard(use_case.get_all_leagues(), ADD_PROFILE_LEAGUE_BUTTON_TEMPLATE)
            + generate_cancel_button(),
        ),
    )
    return ADD_PROFILE_START_ROUTES
