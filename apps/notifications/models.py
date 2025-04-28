from django.db import models
from apps.users.models import User

class Notification(models.Model):
    TYPE_CHOICES = (
        ('reminder', 'Reminder'),
        ('promotion', 'Promotion'),
        ('system', 'System'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=100)
    message = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user.username}"