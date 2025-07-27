from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Message, Conversation, User
from .serializers import (MessageSerializer, UserSerializer,
                          ConversationSerializer)
from django_filters import rest_framework as filters


# Create your views here.

class UserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()

        conversation = message.conversation_id

        if message.sender not in conversation.participants.all():
            conversation.participants.add(message.sender)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({'status': 'Message created successfully'},
                        status=status.HTTP_201_CREATED)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
