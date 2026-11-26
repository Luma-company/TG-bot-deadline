from task_manager import TaskManager
import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
load_dotenv()
token = os.getenv("BOT_TOKEN")
if token is None:
    raise ValueError("Переменная token не найдена")
bot = Bot(token)
dp = Dispatcher()
manager = TaskManager()

manager.add_task(1, "Первая")
manager.add_task(2, "Вторая")

button1 = KeyboardButton(text = "Добавить задачу")
button2 = KeyboardButton(text = "Список задач")
button3 = KeyboardButton(text = "Помощь")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button1, button2],
        [button3]
    ],
    resize_keyboard=True
)

button4 = InlineKeyboardButton(
    text="Выполнить",
    callback_data="carry"
)

button5 = InlineKeyboardButton(
    text="Удалить",
    callback_data="delete"
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button4, button5]
    ]
)

@dp.message(Command("start"))
async def start(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}! Выбирайте:", reply_markup=keyboard)


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Помощь")

@dp.message(F.text == "Добавить задачу")
async def add_task(message: Message):
    await message.answer("Добавляй задачу")

@dp.message(F.text == "Список задач")
async def show_tasks(message: Message):
    for task in manager.get_tasks():
        await message.answer(task.get_info())


@dp.message(F.text == "Помощь")
async def show_help(message: Message):
    await message.answer("Помогаю")

@dp.callback_query(F.data == "carry")
async def carry(callback: CallbackQuery):
    await callback.message.edit_text("Задача выполнена")
    await callback.answer()

@dp.callback_query(F.data == "delete")
async def delete(callback: CallbackQuery):
    await callback.message.edit_text("Удалено")
    await callback.answer()


async def main():
    await dp.start_polling(bot)
asyncio.run(main())
