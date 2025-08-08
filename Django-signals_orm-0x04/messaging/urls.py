from messaging.views import delete_user
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()

router.register('users', delete_user, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
