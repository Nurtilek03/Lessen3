
from aiogram import types
from aiogram.filters import Command, CommandStart
from database import add_user, add_task, add_schedule_time, get_user_schedule, delete_schedule, update_schedule_time
from utils import send_message
from scheduler import scheduler
import asyncio

async def start_command(message: types.Message):
    user_id = message.from_user.id
    cursor = message.bot.cursor
    add_user(cursor, user_id)
    await send_message(message, "Вы успешно зарегистрированы! Используйте команду /task, чтобы добавить задачу.")

async def task_command(message: types.Message):
    await send_message(message, 'Введите задачу:')

    @dp.message(F.text)
    async def save_task(message: types.Message):
        user_id = message.from_user.id
        task = message.text
        cursor = message.bot.cursor
        add_task(cursor, user_id, task)
        await send_message(message, "Задача успешно добавлена! Воспользуйтесь командами: /set_schedule, /view_schedule, /delete_schedule, /update_schedule")

async def set_schedule(message: types.Message):
    await send_message(message, 'Введите время для задачи в формате ЧЧ:ММ')

    @dp.message(F.text)
    async def save_time(message: types.Message):
        user_id = message.from_user.id
        time = message.text
        cursor = message.bot.cursor
        add_schedule_time(cursor, user_id, time)
        await send_message(message, "Время для задачи успешно добавлено.")

async def view_schedule(message: types.Message):
    user_id = message.from_user.id
    cursor = message.bot.cursor
    schedules = get_user_schedule(cursor, user_id)
    if schedules:
        response = "\n".join([f"{time} - {task}" for time, task in schedules])
        await send_message(message, f"Ваше расписание:\n{response}")
    else:
        await send_message(message, "Ваше расписание пусто.")

async def delete_schedule(message: types.Message):
    try:
        time = message.get_args()
        user_id = message.from_user.id
        cursor = message.bot.cursor
        delete_schedule(cursor, user_id, time)
        await send_message(message, f"Задача на {time} удалена.")
    except Exception as e:
        await send_message(message, f"Ошибка: {str(e)}")

async def update_schedule(message: types.Message):
    try:
        args = message.get_args().split()
        old_time, new_time = args
        user_id = message.from_user.id
        cursor = message.bot.cursor
        update_schedule_time(cursor, user_id, old_time, new_time)
        await send_message(message, f"Время уведомления изменено с {old_time} на {new_time}.")
    except Exception as e:
        await send_message(message, f"Ошибка: {str(e)}")
