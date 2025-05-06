from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Progress
from .serializers import ProgressSerializer
from rest_framework.exceptions import ValidationError

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