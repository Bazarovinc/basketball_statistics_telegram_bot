from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import (
    AGREEMENT_AGREE_BUTTON,
    AGREEMENT_AGREE_CALLBACK,
    AGREEMENT_ALREADY_GIVEN_MESSAGE,
    AGREEMENT_MESSAGE,
    AGREEMENT_PDF,
    CANCEL_BUTTON,
    CANCEL_BUTTON_CALLBACK,
    PARSE_MODE,
    USER_COMMAND_CALL,
)
from src.containers.app import UseCasesContainer
from src.domain.use_cases.core_use_cases.user_service import UserService


@inject
async def get_agreement_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
    user_service: UserService = Provide[UseCasesContainer.user_service],
) -> int:
    logger.info(USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id))
    if await user_service.check_user_agreement_exists(update.effective_user.id):
        await update.message.reply_text(
            AGREEMENT_ALREADY_GIVEN_MESSAGE,
            parse_mode=PARSE_MODE,
        )
        return ConversationHandler.END
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(AGREEMENT_AGREE_BUTTON, callback_data=AGREEMENT_AGREE_CALLBACK),
                InlineKeyboardButton(CANCEL_BUTTON, callback_data=CANCEL_BUTTON_CALLBACK),
            ],
        ]
    )
    await update.message.reply_document(document=AGREEMENT_PDF)
    await update.message.reply_text(
        AGREEMENT_MESSAGE,
        parse_mode=PARSE_MODE,
        reply_markup=keyboard,
    )
    return ConversationHandler.END
