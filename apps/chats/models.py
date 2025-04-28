from django.db import models
from apps.users.models import User

class Chat(models.Model):
    chat_name = models.CharField(max_length=100, null=True, blank=True)  # Tên nhóm (cho nhóm chat)
    is_group = models.BooleanField(default=False)  # Phân biệt chat 1-1 và nhóm
    last_message = models.TextField(null=True, blank=True)  # Lưu tin nhắn cuối (cache)
    last_updated = models.DateTimeField(auto_now=True)  # Thời gian cập nhật
    firebase_chat_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Liên kết với Firebase

    def __str__(self):
        return self.chat_name or f"Chat {self.id}"

class ChatParticipant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_participants')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('chat', 'user')  # Đảm bảo không trùng user trong cùng chat

    def __str__(self):
        return f"{self.user.username} in {self.chat}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    firebase_message_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Liên kết với Firebase

    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"