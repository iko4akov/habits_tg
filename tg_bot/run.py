import asyncio
import logging
import os
import sys

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import router

load_dotenv()


async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    dp = Dispatcher()
    bot = Bot(token, parse_mode=ParseMode.HTML)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
