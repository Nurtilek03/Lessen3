# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# import random
# import asyncio, logging
# from config import my_token

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=my_token)

# dp = Dispatcher()

# class OrderState(StatesGroup):
#     waiting_for_category = State()
#     waiting_for_name = State()
#     waiting_for_address = State()
#     waiting_for_details = State()

# orders = {}

# category_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Еда", callback_data="category_food")],
#     [InlineKeyboardButton("Запчасти", callback_data="category_parts")],
#     [InlineKeyboardButton("Мебель", callback_data="category_furniture")]
# ])

# @dp.message_handler(commands="start")
# async def start_command(message: types.Message):
#     await message.answer(
#         "Привет! Выберите категорию заказа:",
#         reply_markup=category_keyboard
#     )
#     await OrderState.waiting_for_category.set()

# @dp.callback_query_handler(state=OrderState.waiting_for_category)
# async def category_selected(callback_query: types.CallbackQuery, state: FSMContext):
#     await state.update_data(category=callback_query.data)
#     await callback_query.message.answer("Введите ваше имя:")
#     await OrderState.waiting_for_name.set()

# @dp.message_handler(state=OrderState.waiting_for_name)
# async def name_received(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Введите адрес доставки:")
#     await OrderState.waiting_for_address.set()

# @dp.message_handler(state=OrderState.waiting_for_address)
# async def address_received(message: types.Message, state: FSMContext):
#     await state.update_data(address=message.text)
#     await message.answer("Введите дополнительную информацию (например, что заказать):")
#     await OrderState.waiting_for_details.set()

# @dp.message_handler(state=OrderState.waiting_for_details)
# async def details_received(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     order_id = random.randint(1000, 9999)
#     orders[order_id] = {
#         "category": user_data["category"],
#         "name": user_data["name"],
#         "address": user_data["address"],
#         "details": message.text,
#         "status": "Заказ принят."
#     }
#     await message.answer(f"Ваш заказ принят! Номер заказа: {order_id}")
#     await state.finish()

# @dp.message_handler(commands="status")
# async def check_status(message: types.Message):
#     try:
#         order_id = int(message.text.split()[1])
#         if order_id in orders:
#             await message.answer(f"Статус заказа {order_id}: {orders[order_id]['status']}")
#         else:
#             await message.answer("Заказ с таким номером не найден.")
#     except (IndexError, ValueError):
#         await message.answer("Пожалуйста, введите команду в формате: /status <номер заказа>")

# # if __name__ == "__main__":
# #     executor.start_polling(dp, skip_updates=True)

# async def main():
#     await dp.start_polling(bot)

# asyncio.run(main())
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# import random
# import asyncio
# import logging
# from config import my_token

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=my_token)
# dp = Dispatcher()

# class OrderState(StatesGroup):
#     waiting_for_category = State()
#     waiting_for_name = State()
#     waiting_for_address = State()
#     waiting_for_details = State()

# orders = {}

# category_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Еда", callback_data="category_food")],
#     [InlineKeyboardButton("Запчасти", callback_data="category_parts")],
#     [InlineKeyboardButton("Мебель", callback_data="category_furniture")]
# ])

# @dp.message_handler(commands="start")
# async def start_command(message: types.Message):
#     await message.answer(
#         "Привет! Выберите категорию заказа:",
#         reply_markup=category_keyboard
#     )
#     await OrderState.waiting_for_category.set()

# @dp.callback_query_handler(state=OrderState.waiting_for_category)
# async def category_selected(callback_query: types.CallbackQuery, state: FSMContext):
#     await state.update_data(category=callback_query.data)
#     await callback_query.message.answer("Введите ваше имя:")
#     await OrderState.waiting_for_name.set()

# @dp.message_handler(state=OrderState.waiting_for_name)
# async def name_received(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Введите адрес доставки:")
#     await OrderState.waiting_for_address.set()

# @dp.message_handler(state=OrderState.waiting_for_address)
# async def address_received(message: types.Message, state: FSMContext):
#     await state.update_data(address=message.text)
#     await message.answer("Введите дополнительную информацию (например, что заказать):")
#     await OrderState.waiting_for_details.set()

# @dp.message_handler(state=OrderState.waiting_for_details)
# async def details_received(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     order_id = random.randint(1000, 9999)
#     orders[order_id] = {
#         "category": user_data["category"],
#         "name": user_data["name"],
#         "address": user_data["address"],
#         "details": message.text,
#         "status": "Заказ принят."
#     }
#     await message.answer(f"Ваш заказ принят! Номер заказа: {order_id}")
#     await state.finish()

# @dp.message_handler(commands="status")
# async def check_status(message: types.Message):
#     try:
#         order_id = int(message.text.split()[1])
#         if order_id in orders:
#             await message.answer(f"Статус заказа {order_id}: {orders[order_id]['status']}")
#         else:
#             await message.answer("Заказ с таким номером не найден.")
#     except (IndexError, ValueError):
#         await message.answer("Пожалуйста, введите команду в формате: /status <номер заказа>")

# async def main():
#     await dp.start_polling(bot)

# asyncio.run(main())