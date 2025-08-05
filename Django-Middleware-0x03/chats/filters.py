import django_filters
from chats.models import Message


class MessageFilter(django_filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            'sender': ['exact'],
            'sent_at': ['range'],
        }
