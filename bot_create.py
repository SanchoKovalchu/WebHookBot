from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import db_conn
storage = MemoryStorage()

##TOKEN_API = "5397374009:AAG5m7j5hSR1IyNAOhqe9vR0Ts27xapzIho"

##Sancho
TOKEN_API = "5302840148:AAGtGfjfQZWbwRn0mqPrv_rEqRhK9XEiarg"

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot, storage=storage)

connection = db_conn.getConnection()
cursor = connection.cursor()

