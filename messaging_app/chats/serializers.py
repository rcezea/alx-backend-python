from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ['password_hash', 'created_at', 'first_name', 'last_name']
        read_only_fields = ['user_id']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()
    class Meta:
        model = Message
        exclude = ['sender', 'conversation']
        read_only_fields = ['message_id', 'sent_at']

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}" if obj.sender else None

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['conversation_id', 'created_at']

    def validate_participants(self, value):
        if not value:
            raise serializers.ValidationError("At least one participant is required.")
        return value
