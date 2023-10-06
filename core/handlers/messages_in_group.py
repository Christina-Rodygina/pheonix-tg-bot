from aiogram.types import Message
from core.main import dp, bot, ID_TSG
from core.filters.chat_types import ChatTypeFilter


@dp.message(ChatTypeFilter(chat_type='private'))
async def reply_message_in_group(message: Message):
    try:
        await bot.send_message(chat_id=ID_TSG, text=f'Сообщение от пользователя:\n'
                                                    f'ID {message.chat.id}\n'
                                                    f'{message.from_user.first_name} {message.from_user.last_name}\n'
                                                    f'\n'
                                                    f'{message.text}')
    except Exception:
        await message.answer('Превышено количество запросов в минуту. Подождите 30 секунд.')


@dp.message(ChatTypeFilter(chat_type='supergroup'))
async def manager_response(message: Message):
    if message.reply_to_message is not None:
        name_manager = message.from_user.first_name
        chat_id = message.reply_to_message.text.split()
        chat_id = chat_id[4]
        await bot.send_message(chat_id=chat_id, text=f'Менеджер: {name_manager}\n'
                                                     f'\n'
                                                     f'{message.text}')
