import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from db import collection
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    logging.info(f"Пользователь {message.from_user}")

    user_data = {
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username
    }
    result = await collection.update_one({'user_id': user.id}, {"$set": user_data}, upsert=True)
    logging.info(f"Result {result}")
    await message.answer(
        f"Hello, {message.from_user.first_name}! "
        f"We're in progress of the development. We'll keep you in touch!"
    )


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
    loop.run_forever()
