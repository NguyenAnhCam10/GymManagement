# apps/users/views.py
from collections.abc import generator

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import User, MemberProfile
from .serializers import UserSerializer, MemberProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Chỉ admin mới thấy tất cả user, user thường chỉ thấy chính mình
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Chỉ admin hoặc chính user mới thấy profile
        if self.request.user.is_superuser:
            return MemberProfile.objects.all()
        return MemberProfile.objects.filter(user=self.request.user)