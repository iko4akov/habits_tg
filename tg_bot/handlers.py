from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from tg_bot.filters import Registration
import tg_bot.keyboards as kb
from tg_bot.db_services import HandlerAPIRequests

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command

    """
    await message.answer(f"Hello", reply_markup=kb.main)


@router.message(F.text == 'Регистрация')
async def register(message: types.Message) -> None:
    await message.reply(f"Введи почту и пароль\nпример:\n<b>test@test.test//password</b>")

@router.message(Registration())
async def get_data(message: types.Message) -> None:
    if '//' in message.text:
        data = {}
        message_list = message.text.split('//')
        data['email'] = message_list[0]
        data['password'] = message_list[1]
        data['telegram_id'] = message.from_user.id
        data['is_active'] = True
        api_handler = HandlerAPIRequests(data)

        if api_handler.create_user():
            await message.reply("Регистрация прошла успешо")
        else:
            await message.answer('что то не так')

@router.message(F.text == 'Получить ID')
async def get_id(message: types.Message):
    await message.answer(f"{message.from_user.id}")

@router.message(F.text == 'Посмотреть все ваши привычки')
async def get_id(message: types.Message):
    data = {}
    data['telegram_id'] = message.from_user.id
    api_handler = HandlerAPIRequests(data)
    habits = api_handler.habit_list_owner()
    if habits is not None:
        for habit in habits:
            await message.answer(habit)
    else:
        await message.answer('У вас нет еще привычек')
@router.message(F.text == 'Посмотреть публичные привычки')
async def get_id(message: types.Message):
    data = {}
    data['telegram_id'] = message.from_user.id
    api_handler = HandlerAPIRequests(data)
    habits = api_handler.habit_list_public()
    if habits is not None:
        for habit in habits:
            await message.answer(str(habit))
    else:
        await message.answer('бежда')

@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer(f'Что то не так, начни с начала -> /start')

    except TypeError:
        await message.answer("Enter /start")



# @router.message(F.text == 'sad')
# async def commands(message: types.Message) -> None:
#     await message.answer(f"Ваш ID: {message.from_user.id}")
#     await message.reply(f"Ваши данные {message.from_user.__dict__}")
#     await message.answer_photo(
#         'https://yandex.ru/images/search?text=картинки&img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2Fe35%2F17332957_1867883113499005_8526655979834572800_n.jpg%3F_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D101%26_nc_ohc%3DoprMtaC8mp0AX_RnE9U%26edm%3DAABBvjUBAAAA%26ccb%3D7-4%26oh%3Db98ff88e072510cdede76e0aa962e84a%26oe%3D61818127%26_nc_sid%3D83d603&pos=0&rpt=simage&stype=image&lr=35&parent-reqid=1696171356622437-4554712149110151382-balancer-l7leveler-kubr-yp-sas-101-BAL-7502&source=serp')
