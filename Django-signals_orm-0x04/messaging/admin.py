from django.contrib import admin
from messaging.models import Message, Notification, MessageHistory

# Register your models here.
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(MessageHistory)
