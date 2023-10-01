from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main_habit = [
    [KeyboardButton(text='Регистрация')],
    [KeyboardButton(text='Создать'), KeyboardButton(text='Редактировать')],
    [KeyboardButton(text='Посмотреть все'), KeyboardButton(text='Посмотреть одну')],
    [KeyboardButton(text='Удалить'), KeyboardButton(text='Посмотреть публичные')]
]

main = ReplyKeyboardMarkup(
    keyboard=main_habit,
    resize_keyboard=True,
    input_field_placeholder='Возможности'
)
