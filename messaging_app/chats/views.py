from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Conversation, User
from .serializers import (MessageSerializer, UserSerializer,
                          ConversationSerializer)


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()

        conversation = message.conversation_id

        if message.sender not in conversation.participants.all():
            conversation.participants.add(message.sender)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
