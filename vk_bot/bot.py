import vk_api
from django.conf import settings
from vk_api.longpoll import VkEventType, VkLongPoll


def main():
    vk_session = vk_api.VkApi(token=settings.VK_GROUP_TOKEN)
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                print('Для меня от: ', event.user_id)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)
