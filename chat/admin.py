from typing import Any, Dict
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Thread, ChatMessage, Notification

# Register your models here.
admin.site.register(ChatMessage)

class ChatMessage(admin.TabularInline):
    model =ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('first_person','second_person')
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Notification )