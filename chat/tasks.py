from celery import shared_task
from accounts.models import User
from chat.models import Notification


@shared_task
def send_notification(message,sender_id, recipient_id):
    sender = User.objects.get(id=sender_id)
    recipient = User.objects.get(id=recipient_id)

    notification = Notification(
        recipient=recipient,
        sender=sender,
        message=message
    )
    notification.save()

