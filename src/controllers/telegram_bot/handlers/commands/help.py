from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import HELP_COMMAND_MESSAGE, PARSE_MODE, USER_COMMAND_CALL


async def get_help_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
) -> int:
    logger.info(USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id))
    await update.message.reply_text(
        HELP_COMMAND_MESSAGE,
        parse_mode=PARSE_MODE,
    )
    return ConversationHandler.END
