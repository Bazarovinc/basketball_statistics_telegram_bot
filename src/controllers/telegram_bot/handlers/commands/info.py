from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import INFO_COMMAND_MESSAGE, USER_COMMAND_CALL


async def get_info_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    logger.info(
        USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id)
    )
    await update.message.reply_text(
        INFO_COMMAND_MESSAGE,
    )
    return ConversationHandler.END
