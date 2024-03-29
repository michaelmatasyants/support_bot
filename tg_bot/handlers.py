from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from django.conf import settings

from .dialogflow import detect_intent_texts

router = Router()


@router.message(Command("start"))
async def process_start(message: Message):
    """Reply to Start command"""
    await message.answer(text="Hello!")


@router.message()
async def process_dialog_flow(message: Message):
    """Replying to a message using the dialog flow"""
    if isinstance(message.text, str):
        text_message = detect_intent_texts(
            project_id=settings.GOOGLE_PROJECT_ID,
            session_id=str(message.chat.id),
            text=message.text,
            fallback=True
        )
        await message.answer(text=text_message)
    else:
        await message.answer(text="Please send a text message.\n"
                                  "Other types are not allowed")
