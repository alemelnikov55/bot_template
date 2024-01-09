from aiogram.types import Message


async def hello(message: Message):
    user = f'{message.from_user.first_name}_{message.from_user.last_name}'
    await message.answer(f'Привет, {user}!')
