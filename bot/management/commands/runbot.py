import asyncio

from django.core.management.base import BaseCommand

from bot import bot


class Command(BaseCommand):
    help = "Start telegram support bot"

    def handle(self, *args, **options):
        asyncio.run(bot.main())
