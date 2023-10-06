from aiogram.types import Message
from core.main import dp, ADMIN_ID, bot
from aiogram.filters import Command
from core.utils.database import registration, check_registration
from core.filters.chat_types import ChatTypeFilter


@dp.message(Command('start'), ChatTypeFilter(chat_type='private'))
async def start(message: Message):
    try:
        await message.answer(f'Приветствую вас!')
        data_deeplink = message.text
        data_deeplink = data_deeplink.split()
        key_data = data_deeplink[1]
        if await check_registration(chat_id=message.chat.id) is True:
            await message.answer('Вы уже зарегистрированы.')
        elif await check_registration(chat_id=message.chat.id) is False and await registration(chat_id=message.chat.id, key_data=key_data):
            await message.answer('Регистрация прошла успешно.')
        else:
            await message.answer('Произошла ошибка при регистрации.')
    except IndexError:
        await message.answer('Повторное использование команды заблокировано.')


@dp.startup()
async def start_bot():
    for admin in ADMIN_ID:
        await bot.send_message(chat_id=admin, text='Бот запущен')
