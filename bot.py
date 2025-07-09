from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    text = (
        "👋 Привет! Я помогу тебе зарабатывать крипту и деньги!\n"
        "🔗 Жми /earn для начала!"
    )
    await msg.reply(text)

@dp.message_handler(commands=['earn'])
async def earn(msg: types.Message):
    await msg.reply(
        f"📌 Вот задания:\n\n"
        f"1️⃣ Установи Honeygain — {config.HONEYGAIN_REF} (получишь $5!)\n"
        f"2️⃣ Кликни краны:\n• FaucetPay: {config.FAUCETPAY_REF}"
        f"\n✅ Зарабатывай легко! Новые задания — каждый день!"
    )

executor.start_polling(dp)
