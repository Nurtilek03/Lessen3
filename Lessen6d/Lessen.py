import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from Lessen6d.app.database import init_db
from Lessen6d.app.handlers import start_command, handle_product, handle_address, handle_phone, handle_confirmation
from Lessen6d.app.states import OrderStates
import os

load_dotenv ()

bot = Bot(token=os.environ.get("my_token"))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

conn, cursor = init_db()

router.message(commands='start')(start_command)
router.message(OrderStates.waiting_for_product)(handle_product)
router.message(OrderStates.waiting_for_address)(handle_address)
router.message(OrderStates.waiting_for_phone)(handle_phone)
router.message(OrderStates.waiting_for_confirmation)(lambda message, state: handle_confirmation(message, state, conn, cursor))

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
