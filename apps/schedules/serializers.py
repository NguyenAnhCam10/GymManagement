from rest_framework import serializers
from .models import Schedule
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.packages.serializers import MemberPackageSerializer
from ..packages.models import MemberPackage


class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pt = UserSerializer(read_only=True)
    member_package = MemberPackageSerializer(read_only=True)
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
    member_package_id = serializers.PrimaryKeyRelatedField(
        queryset=MemberPackage.objects.all(),
        source='member_package',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Schedule
        fields = ['id', 'user', 'user_id', 'pt', 'pt_id', 'member_package', 'member_package_id', 'start_time', 'end_time', 'status', 'note', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']