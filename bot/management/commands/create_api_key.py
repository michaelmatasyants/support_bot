from django.core.management.base import BaseCommand

from bot.create_api_key import main


class Command(BaseCommand):
    help = """Create DIALOGFLOW API key and save with path
              of GOOGLE_APP_CREDENTIALS in '.env' file"""

    def handle(self, *args, **options):
        main()
