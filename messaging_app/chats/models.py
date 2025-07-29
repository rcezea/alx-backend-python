import uuid

from django.db.models import (
    Model, UUIDField, CharField,
    DateTimeField, ForeignKey,
    CASCADE, TextField,
    TextChoices, ManyToManyField
)
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Table """
    class RoleChoices(TextChoices):
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'

    user_id = UUIDField(primary_key=True, db_index=True,
                        default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=256, null=False)
    last_name = CharField(max_length=256, null=False)
    email = CharField(max_length=256, null=False, unique=True)
    password_hash = CharField(max_length=256, null=False)
    phone_number = CharField(max_length=256, null=True)
    role = CharField(max_length=10, choices=RoleChoices.choices,
                     null=False, default=RoleChoices.GUEST)
    created_at = DateTimeField(default=timezone.now)


class Conversation(Model):
    """ Conversation Table """
    conversation_id = UUIDField(primary_key=True, db_index=True,
                                default=uuid.uuid4, editable=False)
    participants = ManyToManyField(User, related_name='conversations',
                                   through='ConversationParticipant',
                                   blank=True)
    created_at = DateTimeField(default=timezone.now)


class Message(Model):
    """ Message Table """
    message_id = UUIDField(primary_key=True, db_index=True,
                           default=uuid.uuid4, editable=False)
    sender = ForeignKey(User, on_delete=CASCADE)
    conversation_id = ForeignKey(Conversation,
                                 on_delete=CASCADE, related_name='messages')
    message_body = TextField(null=False)
    sent_at = DateTimeField(default=timezone.now)


class ConversationParticipant(Model):
    conversation = ForeignKey(
        Conversation, on_delete=CASCADE
    )
    user = ForeignKey(
        User, on_delete=CASCADE
    )

    class Meta:
        db_table = 'chats_conversation_participants'
        unique_together = ('conversation', 'user')
