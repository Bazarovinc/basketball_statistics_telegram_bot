import asyncio

from telegram import CallbackQuery, Update


async def get_callback_query(update: Update) -> CallbackQuery:
    query = update.callback_query
    await asyncio.gather(*(query.answer(), query.delete_message()))
    return query
