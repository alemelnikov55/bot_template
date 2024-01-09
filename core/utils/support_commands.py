from aiogram import Bot

from core.loader import admin_id


async def starting(bot: Bot) -> None:
    await bot.send_message(admin_id, 'Бот запущен')


async def stopping(bot: Bot) -> None:
    await bot.send_message(admin_id, 'Бот остановлен')
