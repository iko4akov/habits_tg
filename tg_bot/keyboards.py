from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main_habit = [
    [KeyboardButton(text='Получить ID')],
    [KeyboardButton(text='Регистрация')],
    [KeyboardButton(text='Посмотреть все ваши привычки')],
    [KeyboardButton(text='Посмотреть публичные привычки')]
]

main = ReplyKeyboardMarkup(
    keyboard=main_habit,
    resize_keyboard=True,
    input_field_placeholder='Возможности'
)
