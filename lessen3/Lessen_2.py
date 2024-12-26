from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
import asyncio, logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import my_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=my_token)


dp = Dispatcher()
router = Router()

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Авто запчасти", callback_data="auto_parts")],
        [InlineKeyboardButton(text="Мобильные запчасти", callback_data="mobile_spare_parts")],
    ])

def auto():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Руль - 1500с", callback_data="Steering_wheel")],
        [InlineKeyboardButton(text="Фары - 3500с", callback_data="Headlights")],
        [InlineKeyboardButton(text="Зеркала - 15000с", callback_data="Mirrors")],
    ])

def mobile():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Чехол - 250с", callback_data="Case")],
        [InlineKeyboardButton(text="Экран - 2500с", callback_data="Screen")],
        [InlineKeyboardButton(text="Батарейка - 1500с", callback_data="Battery")],
    ])

def Agreement():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data="yes")],
        [InlineKeyboardButton(text="Нет", callback_data="No")]
    ])

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Здравствуйте, Добро пожаловать в онлайн магазин",
        reply_markup=get_main_keyboard()
    )

@router.callback_query(lambda callback: callback.data == "auto_parts")
async def handle_auto_parts(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали отправить авто запчасти", reply_markup=auto())
    await callback.answer()

@router.callback_query(lambda callback: callback.data == "yes")
async def agreement(callback: CallbackQuery):
    await callback.message.answer("Ваш заказ оформлень")
    await callback.answer()

@router.callback_query(lambda callback: callback.data == "No")
async def agreement(callback: CallbackQuery):
    await callback.message.answer("Ваш заказ удалина")
    await callback.answer()


@router.callback_query(lambda callback: callback.data == "mobile_spare_parts")
async def handle_mobile_spare_parts(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали отправить мобильные запчасти", reply_markup=mobile())
    await callback.answer()

@router.callback_query(lambda callback: callback.data in ["Steering_wheel", "Headlights", "Mirrors", "Case", "Screen", "Battery"])
async def choose_option(callback_query: CallbackQuery):
    data = callback_query.data
    await callback_query.message.answer('Подтвердите свой выбор:', reply_markup=Agreement())
    await callback_query.answer()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())