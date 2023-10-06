import os

from aiogram import Bot, Dispatcher
import asyncio
import logging
from dotenv import load_dotenv

import core.settings

load_dotenv()

dp = Dispatcher()
TOKEN = str(os.getenv('TOKEN'))
ADMIN_ID = core.settings.admins
bot = Bot(token=TOKEN, parse_mode='HTML')
ID_TSG = core.settings.tsg


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    log_filename = "log_file.log"
    file_handler = logging.FileHandler(log_filename)
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    from handlers import dp
    asyncio.run(main())
