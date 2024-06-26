import asyncio
import logging
from aiogram import Bot, Dispatcher
from telegram_bot.handlers import router
from config_reader import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program forcefully stopped due to KeyboardInterrupt.")
