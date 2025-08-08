from messaging.models import Message, User, Notification, MessageHistory
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=Message)
def create_notification(instance, created, **kwargs):
    if created:
        Notification.objects.create(
            message=instance,
            user=instance.receiver
        )


@receiver(pre_save, sender=Message)
def log_message_history(instance, **kwargs):
    obj = Message.objects.get(id=instance.id)
    latest_version = (MessageHistory.objects.filter(message=instance.id).last())
    latest_version = latest_version.version or 0

    MessageHistory.objects.create(
        message=obj,
        version=latest_version + 1
    )

    instance.edited = True
