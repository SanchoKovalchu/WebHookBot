import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


API_TOKEN = '5302840148:AAGtGfjfQZWbwRn0mqPrv_rEqRhK9XEiarg'

WEBHOOK_HOST = '130.211.226.27:8443'
# WEBHOOK_HOST = '130.211.226.27'
# WEBHOOK_HOST = '130.211.226.27'

WEBHOOK_PATH = ''

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_HOST = '130.211.226.27'  # or ip
WEBAPP_PORT = 8443




logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands="start")
async def echo(message: types.Message):
    # Regular request
    await bot.send_message(message.chat.id, message.text)
    await message.answer("Ласкаво прошу до StudyBot!")

    # or reply INTO webhook
    # return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )