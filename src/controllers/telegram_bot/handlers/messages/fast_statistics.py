import asyncio

from dependency_injector.wiring import Provide, inject
from loguru import logger
from pydantic import AnyHttpUrl, ValidationError
from telegram import InputMediaPhoto, Update
from telegram.ext import ContextTypes, ConversationHandler

from common.exceptions.parsers_exceptions import ServerNotAvailableException, URLValidationException
from src.constants.telegram_templates import (
    BAD_MESSAGE_REPLY_MESSAGE,
    BAD_URL_ERROR_MESSAGE,
    FAST_STATISTICS_RESULT_MESSAGE,
    LEAGUE_SERVER_ERROR_MESSAGE,
    NOT_REPLY_MESSAGE,
    NOT_URL_ERROR_MESSAGE,
    PARSE_MODE,
    WAITING_MESSAGE,
)
from src.containers.use_cases import UseCasesContainer
from src.domain.dto.user_inputs.league_urls import LeagueUrlsUserInputSchema
from src.domain.use_cases.core_use_cases.fast_statistics import FastStatisticsGetter
from src.domain.use_cases.core_use_cases.leagues_service import LeaguesService


@inject
async def get_fast_statistics_result(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    use_case: FastStatisticsGetter = Provide[UseCasesContainer.fast_statistics_getter],
    leagues_service: LeaguesService = Provide[UseCasesContainer.leagues_service],
) -> int:
    user_id = update.effective_user.id
    if not update.message.reply_to_message:
        await context.bot.send_message(
            update.effective_message.chat_id,
            text=NOT_REPLY_MESSAGE,
            parse_mode=PARSE_MODE,
        )
    logger.info(update.message.message_id)
    logger.info(update.message.effect_id)
    user_message = update.message.text
    logger.info(f"Сообщение-ссылка для fast_statistics от пользователя {user_id}")
    logger.debug(f"Ссылка: {user_message}")
    wait_message = await context.bot.send_message(update.effective_message.chat_id, text=WAITING_MESSAGE)
    delete_task = asyncio.ensure_future(
        context.bot.delete_message(chat_id=wait_message.chat_id, message_id=wait_message.message_id)
    )
    try:
        data_from_user = AnyHttpUrl(update.effective_message.text)
    except ValidationError:
        logger.error(f"Пользователь {user_id} прислал не ссылку")
        await asyncio.gather(
            *(
                delete_task,
                context.bot.send_message(update.effective_message.chat_id, text=NOT_URL_ERROR_MESSAGE),
            )
        )
        return ConversationHandler.END
    if league_type := leagues_service.get_league_type_by_fast_statistics(update.message.reply_to_message.text):
        try:
            result = await use_case(LeagueUrlsUserInputSchema(player_url=data_from_user, league_type=league_type))
        except URLValidationException as url_validation_error:
            logger.error(url_validation_error)
            await asyncio.gather(
                *(
                    delete_task,
                    context.bot.send_message(
                        update.effective_message.chat_id,
                        text=BAD_URL_ERROR_MESSAGE,
                        parse_mode=PARSE_MODE,
                    ),
                )
            )
            return ConversationHandler.END
        except ServerNotAvailableException as server_error:
            logger.error(server_error)
            await asyncio.gather(
                *(
                    delete_task,
                    context.bot.send_message(
                        update.effective_message.chat_id,
                        text=LEAGUE_SERVER_ERROR_MESSAGE,
                        parse_mode=PARSE_MODE,
                    ),
                )
            )
            return ConversationHandler.END
    else:
        await asyncio.gather(
            *(
                delete_task,
                context.bot.send_message(
                    update.effective_message.chat_id,
                    text=BAD_MESSAGE_REPLY_MESSAGE,
                    parse_mode=PARSE_MODE,
                ),
            )
        )
        return ConversationHandler.END
    images = [InputMediaPhoto(image, caption=title) for image, title in result.images]
    logger.info("Отправка графиков")
    await asyncio.gather(
        *(
            context.bot.send_message(
                update.effective_message.chat_id,
                text=FAST_STATISTICS_RESULT_MESSAGE.format(username=result.username, league=result.league.value),
                parse_mode=PARSE_MODE,
            ),
            context.bot.send_media_group(update.effective_message.chat_id, images),
        )
    )
    await delete_task
    return ConversationHandler.END
