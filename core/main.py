import asyncio
from aiogram import Dispatcher, F, Bot
from aiogram.filters import Command
from aiogram_calendar import SimpleCalendarCallback

from loader import TOKEN
from core.utils.support_commands import starting, stopping
from handlers.hello import hello
from handlers.date_from_user import data_from_user, change_state
from core.calendars.calendar_handler import command_start_handler, nav_cal_handler, \
    process_simple_calendar
from core.states.insert_data import StateInsertDate


async def start_bot() -> None:
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.callback_query.register(process_simple_calendar, SimpleCalendarCallback.filter())
    dp.startup.register(starting)
    dp.shutdown.register(stopping)
    dp.message.register(hello, Command(commands='hello'))
    dp.message.register(command_start_handler, Command(commands='start'))
    dp.message.register(nav_cal_handler, F.text.lower() == 'navigation calendar')
    # dp.message.register(data_from_user, F.text.startswith('0'))
    dp.message.register(change_state, F.text == 'Ввести дату в формате дд.мм')
    dp.message.register(data_from_user, StateInsertDate.show_time)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
