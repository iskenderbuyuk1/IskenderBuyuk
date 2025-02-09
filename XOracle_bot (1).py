import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Muhit o'zgaruvchilarini yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# WebApp URL (Vercel'dagi sayt manzili)
WEBAPP_URL = "https://iskender-buyuk.vercel.app/"

# /start buyrug‘i uchun handler
@dp.message(Command("start"))
async def start_handler(message: Message):
    # Klaviatura tugmalari
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔮 Oraclega kirish", web_app=WebAppInfo(url=WEBAPP_URL))] # WebApp tugmasi
        ],
        resize_keyboard=True
    )

    # Inline tugma (xabar ichida)
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔮 Oraclega kirish", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )

    # Xabarni yuborish
    await message.answer(
        "Salom! XOracle botiga xush kelibsiz! 🔥\nPastdagi tugma orqali mini ilovani oching!",
        reply_markup=keyboard
    )
    await message.answer("Yoki quyidagi tugma orqali ham kirishingiz mumkin:", reply_markup=inline_keyboard)

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())