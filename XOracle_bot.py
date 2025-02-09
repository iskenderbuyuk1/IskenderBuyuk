import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Muhit o'zgaruvchilarini yuklaymiz (.env fayldan)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start buyrug‘iga javob (Mini App tugmasi bilan)
@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔮 Oraclega kirish", web_app=WebAppInfo(url="https://example.com"))]
        ],
        resize_keyboard=True
    )
    await message.answer("Salom! XOracle botiga xush kelibsiz! 🔥\nPastdagi tugma orqali mini ilovani oching!", reply_markup=keyboard)

# Mini App-dan botga yuborilgan ma'lumotlarni qabul qilish
@dp.message()
async def receive_webapp_data(message: Message):
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"Mini app-dan kelgan ma'lumot: {data}")

# Botni ishga tushirish funksiyasi
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())