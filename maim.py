import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

bot = Bot("9108817894:AAG8EIwURTpnpTe5lCnJLMd6VzUVF54uVOo")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет")

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Помощь")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())