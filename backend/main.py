import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from backend.messages import (
    get_help_message,
    get_support_message,
    get_unacceptable_message,
    get_welcome_message,
)
from db import collection
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def welcome(message: types.Message):
    user = message.from_user
    logging.info(f"Пользователь {user.username}")

    user_data = {
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username
    }
    await collection.update_one({'user_id': user.id}, {"$set": user_data}, upsert=True)
    await message.answer(
        await get_welcome_message(user.language_code, user.first_name),
        reply_markup=types.ReplyKeyboardRemove(),
    )


@dp.message(Command("help"))
async def commands(message: types.Message):
    buttons = [
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/start'),
            KeyboardButton(text='❤️'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите комманду"
    )
    await message.answer(
        await get_help_message(message.from_user.language_code),
        reply_markup=keyboard,
    )


@dp.message(F.text == '❤️')
async def unacceptable(message: types.Message):
    await message.answer(
        await get_support_message(message.from_user.language_code),
        reply_markup=types.ReplyKeyboardRemove(),
    )


@dp.message()
async def unacceptable(message: types.Message):
    logging.info(f"Пользователь {message.text}")
    await message.answer(
        await get_unacceptable_message(message.from_user.language_code),
        reply_markup=types.ReplyKeyboardRemove(),
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.run_polling(bot))
    loop.run_forever()
