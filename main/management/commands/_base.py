from telegram.ext import Updater, Application
from django.core.management.base import BaseCommand
from django.conf import settings
import asyncio


class BotBase(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(BotBase, self).__init__(*args, **kwargs)

        self.application = Application.builder().token(settings.BOT_TOKEN).build()


class ParserBase(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(ParserBase, self).__init__(*args, **kwargs)
    
