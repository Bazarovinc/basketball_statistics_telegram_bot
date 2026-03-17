from loguru import logger
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import (
    CANCEL_BUTTON,
    CANCEL_BUTTON_CALLBACK,
    DELETE_PROFILE_CONFIRM_BUTTON,
    DELETE_PROFILE_CONFIRM_CALLBACK,
    DELETE_PROFILE_WARNING_MESSAGE,
    PARSE_MODE,
    USER_COMMAND_CALL,
)


async def get_delete_profile_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
) -> int:
    logger.info(USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id))
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(DELETE_PROFILE_CONFIRM_BUTTON, callback_data=DELETE_PROFILE_CONFIRM_CALLBACK),
                InlineKeyboardButton(CANCEL_BUTTON, callback_data=CANCEL_BUTTON_CALLBACK),
            ],
        ]
    )
    await update.message.reply_text(
        DELETE_PROFILE_WARNING_MESSAGE,
        parse_mode=PARSE_MODE,
        reply_markup=keyboard,
    )
    return ConversationHandler.END
