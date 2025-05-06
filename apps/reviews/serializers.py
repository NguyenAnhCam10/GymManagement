from rest_framework import serializers
from .models import Review
from apps.users.serializers import UserSerializer
from ..users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pt = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='member'),
        source='user',
        write_only=True
    )
    pt_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='pt'),
        source='pt',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_id', 'pt', 'pt_id', 'gym_rating', 'pt_rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']