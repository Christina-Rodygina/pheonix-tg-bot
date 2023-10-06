from core.main import bot, dp
from core.utils.database import check_key


async def notification(key_data, text):
    chat_id = await check_key(key_data=key_data)
    if chat_id is not None:
        chat_id = int(chat_id[0])
        await bot.send_message(chat_id=chat_id, text=f'{text}')
    else:
        return None
