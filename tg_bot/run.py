import asyncio
import logging
import os
import sys

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from tg_bot.handlers import router

load_dotenv()
token = os.getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(token, parse_mode=ParseMode.HTML)

async def send_message_to_user(user_id, text):
    try:
        await bot.send_message(chat_id=user_id, text=text)
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
