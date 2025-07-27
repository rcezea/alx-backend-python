from django.urls import path, include
from .views import MessageViewSet, UserViewSet, ConversationViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('messages', MessageViewSet, basename='message')
router.register('conversations', ConversationViewSet, basename='conversation')

urlpatterns = [
    path('', include(router.urls)),
]
