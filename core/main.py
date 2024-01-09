import asyncio
from aiogram import Dispatcher, F, Bot
from aiogram.filters import Command

from loader import TOKEN
from core.utils.support_commands import starting, stopping
from handlers.hello import hello


async def start_bot() -> None:
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(starting)
    dp.shutdown.register(stopping)
    dp.message.register(hello, Command(commands='hello'))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
