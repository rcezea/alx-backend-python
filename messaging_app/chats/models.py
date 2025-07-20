import uuid

from django.db.models import Model, UUIDField, CharField, DateTimeField, ForeignKey, CASCADE, TextField, TextChoices, ManyToManyField
from django.utils import timezone


# Create your models here.


class RoleChoices(TextChoices):
    GUEST = 'guest', 'Guest'
    HOST = 'host', 'Host'
    ADMIN = 'admin', 'Admin'

class User(Model):
    """ User Table """
    user_id = UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=256, null=False)
    last_name = CharField(max_length=256, null=False)
    email = CharField(max_length=256, null=False, unique=True)
    password_hash = CharField(max_length=256, null=False)
    phone_number = CharField(max_length=256, null=True)
    role = CharField(max_length=10, choices=RoleChoices.choices, null=False)
    created_at = DateTimeField(default=timezone.now)


class Message(Model):
    """ Message Table """
    message_id = UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    sender_id = ForeignKey(User, on_delete=CASCADE)
    conversation_id = ForeignKey('Conversation', on_delete=CASCADE, related_name='messages')
    message_body = TextField(null=False)
    sent_at = DateTimeField(default=timezone.now)


class Conversation(Model):
    """ Conversation Table """
    conversation_id = UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    participants = ManyToManyField(User, related_name='conversations')
    created_at = DateTimeField(default=timezone.now)
