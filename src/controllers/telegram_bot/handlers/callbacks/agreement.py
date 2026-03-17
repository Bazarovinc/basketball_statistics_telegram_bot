import asyncio

from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes

from src.constants import AGREEMENT_AGREED_MESSAGE, PARSE_MODE
from src.containers.app import UseCasesContainer
from src.controllers.telegram_bot.utils.get_callback_query import get_callback_query
from src.domain.dto.input.user import UserInSchema
from src.domain.use_cases.core_use_cases.user_service import UserService


@inject
async def get_agreement_agree_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
    user_service: UserService = Provide[UseCasesContainer.user_service],
) -> None:
    message_id = update.callback_query.message.message_id
    await asyncio.gather(
        *(
            get_callback_query(update),
            user_service.add_user_agreement(
                UserInSchema(tg_id=update.effective_user.id, tg_username=update.effective_user.username), message_id
            ),
        )
    )
    logger.info(f"Пользователь {update.effective_user.id} нажал кнопку «Согласен» (message_id={message_id})")
    await update.effective_message.reply_text(AGREEMENT_AGREED_MESSAGE, parse_mode=PARSE_MODE)
