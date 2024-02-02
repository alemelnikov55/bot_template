from aiogram.filters.state import State, StatesGroup


class StateInsertDate(StatesGroup):
    show_time = State()
