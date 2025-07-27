from .views import MessageViewSet, UserViewSet, ConversationViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('messages', MessageViewSet, basename='message')
router.register('conversations', ConversationViewSet, basename='conversation')

urlpatterns += router.urls
