from aiogram import Dispatcher
from aiogram.types import Message


# Этот хэндлер будет реагировать на любые текстовые сообщения пользователя
async def send_echo(message: Message):
    await message.answer('Я не понимаю эту команду(')


# Функция для регистрации хэндлера
def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)