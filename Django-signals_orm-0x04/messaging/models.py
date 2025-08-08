from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', null=False, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', null=False, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content[:10]}..."

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)