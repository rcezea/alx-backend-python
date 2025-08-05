from rest_framework import serializers
from .models import User, Conversation, Message
from django.contrib.auth.models import AbstractUser


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone_number = serializers.CharField(required=False,
                                         allow_blank=True)

    class Meta:
        model = User
        exclude = ['password_hash', 'created_at']
        read_only_fields = ['user_id', 'created_at']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['message_id', 'sent_at', 'sender']

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)  # Accept a 'fields' kwarg
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Keep only the requested fields
            for field in set(self.fields) - set(fields):
                self.fields.pop(field)

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"\
            if obj.sender else None

    def validate_sender(self, value):
        request = self.context.get('request')
        if request and value != request.user:
            raise serializers.ValidationError(
                f"You can only send messages as {request.user}.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'created_at', 'messages', 'participants']
        read_only_fields = ['created_at']

    def get_messages(self, obj):
        messages = obj.messages.all()
        serializer = MessageSerializer(messages,
                                       many=True, context=self.context,
                                       fields=['sender_name', 'message_body'])
        return serializer.data

    def validate_participants(self, value):
        if not value:
            raise serializers.ValidationError(
                "At least one participant is required.")
        return value


"""
A cleaner way to customize the output
for messages in a conversation will be
to create a dedicated serializer just for that
"""

# class ConversationMessageSerializer(serializers.ModelSerializer):
#     sender_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Message
#         fields = ['sender_name', 'message_body']
#
#     def get_sender_name(self, obj):
#         return f"{obj.sender.first_name} {obj.sender.last_name}" \
#         if obj.sender else None
