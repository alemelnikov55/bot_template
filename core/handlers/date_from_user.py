import datetime

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.time_sektions_kb import time_section_kb
from core.states.insert_data import StateInsertDate


async def change_state(message: Message, state: FSMContext):
    await state.set_state(StateInsertDate.show_time)


async def data_from_user(message: Message, state: FSMContext):
    selected_month = int(message.text.split('.')[0])
    selected_day = int(message.text.split('.')[1])
    current_year = datetime.date.today().year
    date = datetime.date(year=current_year, month=selected_month, day=selected_day)
    """
    Проверка есть ли свободное время в этот день
    """
    await message.answer('Дату проверили и утачнили есть ли свободные даты.', reply_markup=time_section_kb)