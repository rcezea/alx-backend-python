from django.shortcuts import render
from rest_framework import viewsets
from messaging.models import User
from messaging.serializers import UserSerializer

# Create your views here.


class delete_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
