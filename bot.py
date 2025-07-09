from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
import asyncio
import config

# Инициализация
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

# Команда /start
@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("👋 Привет! Я бот для пассивного дохода.\nНажми /earn чтобы получить задания.")

# Команда /earn
@router.message(commands=["earn"])
async def earn_handler(message: Message):
    links = [
        "<b>📱 Honeygain</b>: <a href='https://r.honeygain.me/DATELCF308'>Перейти по ссылке</a>",
        "<b>💰 FaucetPay</b>: <a href='https://faucetpay.io/?r=9207641'>Получать крипту</a>"
    ]
    await message.answer("\n\n".join(links), disable_web_page_preview=True)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
