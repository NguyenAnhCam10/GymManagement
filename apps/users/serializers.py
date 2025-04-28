# apps/users/serializers.py
from rest_framework import serializers
from .models import User, MemberProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'role', 'created_at', 'last_login')

class MemberProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = MemberProfile
        fields = ('id', 'user', 'height', 'weight', 'bmi', 'updated_at')