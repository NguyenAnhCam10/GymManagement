from rest_framework import serializers
from .models import Progress
from apps.users.serializers import UserSerializer
from ..users.models import User


class ProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pt = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    pt_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='pt', write_only=True, allow_null=True
    )

    class Meta:
        model = Progress
        fields = ['id', 'user', 'user_id', 'pt', 'pt_id', 'weight', 'body_fat', 'muscle_mass', 'note', 'recorded_at']
        read_only_fields = ['pt', 'recorded_at']

