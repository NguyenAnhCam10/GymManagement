from rest_framework import serializers
from .models import Package, MemberPackage
from apps.users.serializers import UserSerializer

class PackageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Package
        fields = ['id', 'name', 'price', 'description', 'pt_sessions', 'package_type', 'created_by', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
class MemberPackageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    package = PackageSerializer(read_only=True)
    package_id = serializers.PrimaryKeyRelatedField(
        queryset=Package.objects.filter(is_active=True), source='package', write_only=True
    )

    class Meta:
        model = MemberPackage
        fields = ['id', 'user', 'package', 'package_id', 'start_date', 'end_date', 'remaining_sessions', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'end_date', 'remaining_sessions', 'status', 'created_at', 'updated_at']