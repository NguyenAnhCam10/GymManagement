from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.exceptions import ValidationError

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