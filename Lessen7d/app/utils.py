from aiogram.types import Message

async def send_message(message: Message, text: str):
    await message.answer(text)
