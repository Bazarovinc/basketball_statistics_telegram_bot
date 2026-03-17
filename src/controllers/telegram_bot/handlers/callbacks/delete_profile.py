from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes

from src.constants import DELETE_PROFILE_SUCCESS_MESSAGE, PARSE_MODE
from src.containers.app import UseCasesContainer
from src.controllers.telegram_bot.utils.get_callback_query import get_callback_query
from src.domain.use_cases.core_use_cases.user_service import UserService


@inject
async def get_delete_profile_confirm_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
    user_service: UserService = Provide[UseCasesContainer.user_service],
) -> None:
    await get_callback_query(update)
    tg_id = update.effective_user.id
    logger.info(f"Пользователь {tg_id} подтвердил удаление профиля")
    await user_service.delete_user(tg_id)
    await update.effective_message.reply_text(DELETE_PROFILE_SUCCESS_MESSAGE, parse_mode=PARSE_MODE)
