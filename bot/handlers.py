from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def process_start(message: Message):
    await message.answer(text='Hello!')


@router.message()
async def process_echo(message: Message):
    if isinstance(message.text, str):
        await message.answer(text=message.text)
    else:
        await message.answer(text='Please send a text message.\n'
                                  'Other types are not allowed')
