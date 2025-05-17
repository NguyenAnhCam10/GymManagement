from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, MemberProfile, Package, MemberPackage, Schedule, Review, Progress, Payment, Notification, Chat, Message
from .serializers import UserSerializer, MemberProfileSerializer, ScheduleSerializer, PackageSerializer, MemberPackageSerializer
from .serializers import ReviewSerializer, ProgressSerializer, PaymentSerializer, NotificationSerializer, ChatSerializer, MessageSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import action
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

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MemberPackageViewSet(viewsets.ModelViewSet):
    queryset = MemberPackage.objects.all()
    serializer_class = MemberPackageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return MemberPackage.objects.all()
        return MemberPackage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Schedule.objects.all()
        elif self.request.user.role == 'pt':
            return Schedule.objects.filter(pt=self.request.user)
        return Schedule.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.role == 'pt':
            serializer.save(pt=self.request.user)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user.role == 'pt':
            serializer.save()
        elif self.request.user == instance.user:
            serializer.save(status='pending')  # Hội viên cập nhật thì status về pending
        else:
            raise ValidationError("You do not have permission to update this schedule.")

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Review.objects.all()
        elif self.request.user.role == 'pt':
            return Review.objects.filter(pt=self.request.user)
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.role != 'member':
            raise ValidationError("Only members can create reviews.")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user != instance.user:
            raise ValidationError("You can only update your own reviews.")
        serializer.save()

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Progress.objects.all()
        elif self.request.user.role == 'pt':
            return Progress.objects.filter(pt=self.request.user)
        return Progress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.role != 'pt':
            raise ValidationError("Only PTs can create progress records.")
        serializer.save(pt=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user != instance.pt:
            raise ValidationError("You can only update progress records you created.")
        serializer.save()


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Chỉ hiển thị notification của người dùng hiện tại (trừ admin)
        user = self.request.user
        if user.is_superuser:
            return Notification.objects.all()
        return Notification.objects.filter(user=user)

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        chat = self.get_object()
        messages = chat.messages.all().order_by('-timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

