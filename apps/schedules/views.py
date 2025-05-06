from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.exceptions import ValidationError

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