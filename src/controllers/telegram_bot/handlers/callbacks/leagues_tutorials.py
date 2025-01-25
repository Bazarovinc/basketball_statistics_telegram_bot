import asyncio

from dependency_injector.wiring import Provide, inject
from loguru import logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from src.constants import FAST_STATISTICS_TUTORIAL_MESSAGE
from src.containers.use_cases import UseCasesContainer
from src.controllers.telegram_bot.utils import generate_tutorial_photos_group
from src.controllers.telegram_bot.utils.get_callback_query import get_callback_query
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_fast_statistic_tutorial_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    query = await get_callback_query(update)
    logger.info(f"Пользователь {update.effective_user.id} нажал кнопку {query.data}")
    league_info = use_case.get_league_by_id(query.data)
    await asyncio.gather(
        *(
            context.bot.send_message(
                chat_id=update.effective_message.chat_id,
                text=FAST_STATISTICS_TUTORIAL_MESSAGE,
            ),
            context.bot.send_media_group(
                chat_id=update.effective_message.chat_id,
                media=generate_tutorial_photos_group(
                    league_info.fast_statistic_tutorial.screenshots
                ),
            ),
        )
    )
    return ConversationHandler.END
