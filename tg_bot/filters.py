import re

from aiogram import types
from aiogram.filters import Filter


class Registration(Filter):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    async def __call__(self, message: types.Message):
        return self.pattern.findall(message.text)
