import random

import vk_api as vk
from django.conf import settings
from vk_api.longpoll import VkEventType, VkLongPoll

from tg_bot.dialogflow import detect_intent_texts


def echo(event, vk_api):
    """Echo the message from user to vk group"""
    vk_api.messages.send(
         user_id=event.user_id,
         message=event.text,
         random_id=random.randint(1, 1000)
    )


def process_dialog_flow(event, vk_api):
    """Replying to a message using the dialog flow"""
    text_message = detect_intent_texts(
        project_id=settings.GOOGLE_PROJECT_ID,
        session_id=event.user_id,
        text=event.text
    )
    vk_api.messages.send(user_id=event.user_id,
                         message=text_message,
                         random_id=random.randint(1, 1000))


def main():
    """Main function"""
    vk_session = vk.VkApi(token=settings.VK_GROUP_TOKEN)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            process_dialog_flow(event, vk_api)
