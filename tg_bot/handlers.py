import re

from aiogram import Router, F, types
from aiogram.client import bot
from aiogram.filters import CommandStart
from aiogram.types import Message


import keyboards as kb

router = Router()

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command

    """
    await message.answer(f"Hello", reply_markup=kb.main)


@router.message(F.text == 'Регистрация')
async def register(message: types.Message) -> None:
    await message.reply(f"введи свою почту и пароль через пробел")

@router.callback_query()
async def register(callback: CallbackQuery) -> None:
    pattern.findall(message.text)
    await message.reply(f"Почта получена, Введите пароль")

@router.message(F.text == 'sad')
async def commands(message: types.Message) -> None:
    await message.answer(f"Ваш ID: {message.from_user.id}")
    await message.reply(f"Ваши данные {message.from_user.__dict__}")
    await message.answer_photo(
        'https://yandex.ru/images/search?text=картинки&img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2Fe35%2F17332957_1867883113499005_8526655979834572800_n.jpg%3F_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D101%26_nc_ohc%3DoprMtaC8mp0AX_RnE9U%26edm%3DAABBvjUBAAAA%26ccb%3D7-4%26oh%3Db98ff88e072510cdede76e0aa962e84a%26oe%3D61818127%26_nc_sid%3D83d603&pos=0&rpt=simage&stype=image&lr=35&parent-reqid=1696171356622437-4554712149110151382-balancer-l7leveler-kubr-yp-sas-101-BAL-7502&source=serp')


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Enter /start")