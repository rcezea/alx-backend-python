from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from .views import MessageViewSet, UserViewSet, ConversationViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('messages', MessageViewSet, basename='message')
router.register('conversations', ConversationViewSet, basename='conversation')

# Nested router: messages under conversations
conversation_router = NestedDefaultRouter(router, 'conversations', lookup='conversation')
conversation_router.register('messages', MessageViewSet, basename='conversation-messages')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),  # <-- Include nested URLs

]
