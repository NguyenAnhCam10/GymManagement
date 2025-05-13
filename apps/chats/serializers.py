
from rest_framework import serializers
from .models import Chat, ChatParticipant, Message
from apps.users.models import User

class ChatParticipantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChatParticipant
        fields = ['id', 'chat', 'user', 'joined_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'timestamp', 'firebase_message_id']

class ChatSerializer(serializers.ModelSerializer):
    participants = ChatParticipantSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'chat_name', 'is_group', 'last_message', 'last_updated', 'firebase_chat_id', 'participants', 'messages']
