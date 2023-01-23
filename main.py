from aiogram import Bot, Dispatcher, executor, types
from random import randint


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)
number: int

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
    global number
    number = randint(0, 100)
    await message.answer('Привет!\nЯ загадал число от 0 до 100!\nПопробуешь угадать?')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: types.Message):
    await message.answer('Для начала игры в угадайку отправь /start')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def guess_the_number(message: types.Message):
    mess = message.text
    if mess.isdigit() and int(mess) in range(0, 100):
        mess = int(mess)
        if mess > number:
            await message.answer('Моё число меньше ;)')
        elif mess < number:
            await message.answer('Моё число больше ;)')
        else:
            await message.answer('Вы угадали число!')
    else:
        await message.answer('Введите число от 0 до 100')




# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(guess_the_number)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)