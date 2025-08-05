import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import lorem_ipsum
from chats.models import User, Conversation, Message

class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        conversations = Conversation.objects.filter(participants__conversations__isnull=True)
        conversations.delete()
