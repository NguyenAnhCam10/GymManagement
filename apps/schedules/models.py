from django.db import models
from apps.users.models import User

class Schedule(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    pt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pt_schedules', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.start_time}"