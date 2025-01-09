from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher import Router
from database import save_order_to_db
from states import OrderStates
from utils import send_message

# Обработчик команды /start
async def start_command(message: types.Message, state: FSMContext):
    await send_message(message, "Добро пожаловать! Какой товар вы хотите заказать?")
    await state.set_state(OrderStates.waiting_for_product)

# Обработчик ввода товара
async def handle_product(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await send_message(message, "Введите адрес доставки:")
    await state.set_state(OrderStates.waiting_for_address)

# Обработчик ввода адреса
async def handle_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await send_message(message, "Введите ваш номер телефона:")
    await state.set_state(OrderStates.waiting_for_phone)

# Обработчик ввода телефона
async def handle_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()

    confirmation_message = (
        f"Пожалуйста, подтвердите ваш заказ:\n"
        f"Товар: {user_data['product']}\n"
        f"Адрес доставки: {user_data['address']}\n"
        f"Телефон: {user_data['phone']}\n"
        "Напишите 'подтвердить' для подтверждения или 'отменить' для отмены."
    )
    await send_message(message, confirmation_message)
    await state.set_state(OrderStates.waiting_for_confirmation)

# Обработчик подтверждения или отмены заказа
async def handle_confirmation(message: types.Message, state: FSMContext, conn, cursor):
    user_data = await state.get_data()  # Получаем данные, введённые пользователем
    if message.text.lower() == 'подтвердить':
        save_order_to_db(conn, cursor, user_data, message.from_user.id)
        await send_message(message, "Ваш заказ подтверждён! Спасибо за покупку.")
        await state.finish()  # Завершаем состояние
    elif message.text.lower() == 'отменить':
        await send_message(message, "Ваш заказ отменён.")
        await state.finish()  # Завершаем состояние
    else:
        await send_message(message, "Пожалуйста, напишите 'подтвердить' или 'отменить'.")
