"""
Module for DRF API Views
"""

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message, Conversation, User, ConversationParticipant
from .serializers import (MessageSerializer, UserSerializer,
                          ConversationSerializer)
from django_filters import rest_framework as filters
from chats.permissions import IsSenderOfMessage, IsParticipantOfConversation


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

    def get_queryset(self):
        return Message.objects.filter(
            conversation_id__participants=self.request.user)

    def perform_create(self, serializer):
        message = serializer.save(sender=self.request.user)
        conversation = message.conversation_id
        if message.sender not in conversation.participants.all():
            conversation.participants.add(message.sender)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['sender'] = str(request.user.pk)
        # or `request.user.id`

        # Check and Create New Conversation IF NOT EXISTS
        """if not data.get('conversation_id'):
            # print('Error due to parallax')
            conversation = Conversation.objects.create()
            data['conversation_id'] = conversation.conversation_id"""
        # NOT REQUIRED SO COMMENT OUT

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAuthenticated(), IsParticipantOfConversation()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsSenderOfMessage()]
        return [IsAuthenticated()]


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        # Return only conversations where the user is a participant
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):

        participants = request.data.get("participants", [])
        if isinstance(participants, str):
            participants = request.data.getlist("participants")

        if not participants or len(participants) < 2:
            return Response(
                {"error": "A conversation must have at least 2 participants."},
                status=status.HTTP_400_BAD_REQUEST
            )
        users = User.objects.filter(user_id__in=participants)
        conversation = Conversation.objects.create()
        for user in users:
            (ConversationParticipant.objects
             .create(conversation=conversation, user=user))
        conversation.participants.set(users)

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsParticipantOfConversation()]
        return [IsAuthenticated()]
