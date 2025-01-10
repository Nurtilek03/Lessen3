
import aioschedule
from datetime import datetime
from bot import bot
from database import get_user_schedule

async def send_reminder():
    cursor = bot.cursor  # Используется глобальный курсор из bot.py
    schedules = cursor.execute("SELECT user_id, time, task FROM schedules").fetchall()
    for user_id, time, task in schedules:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == time:
            await bot.send_message(user_id, f"Пора выполнить задачу: {task}")

async def scheduler():
    aioschedule.every().minute.do(send_reminder)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
