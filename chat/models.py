from django.db import models
from accounts.models import User
# Create your models here.

class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =['first_person', 'second_person']

# class ChatMessage(models.Model):
#     thread = models.ForeignKey(Thread, null=True, blank=True)