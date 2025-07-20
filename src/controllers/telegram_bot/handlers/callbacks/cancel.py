from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.controllers.telegram_bot.utils.get_callback_query import get_callback_query


async def get_cancel_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
) -> int:
    query = await get_callback_query(update)
    logger.info(f"Пользователь {update.effective_user.id} нажал кнопку {query.data}")
    return ConversationHandler.END
