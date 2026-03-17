from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import PARSE_MODE, START_COMMAND_MESSAGE, USER_COMMAND_CALL
from src.containers.app import UseCasesContainer
from src.domain.dto.input.user import UserInSchema
from src.domain.use_cases.core_use_cases.user_service import UserService


@inject
async def get_start_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: ARG001
    user_service: UserService = Provide[UseCasesContainer.user_service],
) -> int:
    logger.info(USER_COMMAND_CALL.format(command=update.message.text, user_id=update.effective_user.id))
    await user_service.create_user(
        UserInSchema(tg_id=update.effective_user.id, tg_username=update.effective_user.username)
    )
    await update.message.reply_text(START_COMMAND_MESSAGE, parse_mode=PARSE_MODE)
    return ConversationHandler.END
