from django.core.management.base import BaseCommand

from vk_bot import bot


class Command(BaseCommand):
    help = "Start vk support bot"

    def handle(self, *args, **options):
        bot.main()
