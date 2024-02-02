import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TIME_SECTIONS = (
    (10, 11),
    (11, 12),
    (12, 13),
    (13, 14),
    (14, 15)
)

time_section_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{sector[0]}:00 - {sector[1]}:00",
                              callback_data=f'{sector[0]}-{sector[1]}')] for sector in TIME_SECTIONS]
)

#f"{datetime.time(hour=sector[0]).strftime('%h')}"
#, callback_data=f'{sector[0]}-{sector[1]}'
#, {datetime.time(hour=sector[1]).strftime('%h')}
# print(time_section_kb)
