
# import asyncio
# from aiogram import Bot, Dispatcher
# from config import my_token
# from Lessen7d.app.handlers import start_command, task_command, set_schedule, view_schedule, delete_schedule, update_schedule
# from Lessen7d.app.database import init_db
# from Lessen7d.app.scheduler import scheduler

# bot = Bot(token=my_token)
# dp = Dispatcher()

# connect, cursor = init_db()


# dp.message(commands="start")(start_command)
# dp.message(commands="task")(task_command)
# dp.message(commands="set_schedule")(set_schedule)
# dp.message(commands="view_schedule")(view_schedule)
# dp.message(commands="delete_schedule")(delete_schedule)
# dp.message(commands="update_schedule")(update_schedule)

# async def on_start():
#     await asyncio.gather(
#         dp.start_polling(),
#         scheduler()
#     )

# if __name__ == "__main__":
#     asyncio.run(on_start())
