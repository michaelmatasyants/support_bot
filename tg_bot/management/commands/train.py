from django.core.management.base import BaseCommand

from tg_bot.dialogflow import create_intents


class Command(BaseCommand):
    help = """Trains the dialog flow using the train_dialogflow.json file"""

    def handle(self, *args, **options):
        create_intents()
