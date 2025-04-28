# apps/chats/admin.py
from django.contrib import admin
from .models import Chat, ChatParticipant, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_name', 'is_group', 'last_message', 'last_updated')
    list_filter = ('is_group',)
    search_fields = ('chat_name',)

@admin.register(ChatParticipant)
class ChatParticipantAdmin(admin.ModelAdmin):
    list_display = ('chat', 'user', 'joined_at')
    list_filter = ('chat',)
    search_fields = ('user__username',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'content', 'timestamp')
    list_filter = ('chat', 'sender')
    search_fields = ('content', 'sender__username')
