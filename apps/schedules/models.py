from django.db import models
from apps.users.models import User
from apps.packages.models import MemberPackage

class Schedule(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='schedules',
        limit_choices_to={'role': 'member'}
    )
    pt = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pt_schedules',
        null=True,
        blank=True,
        limit_choices_to={'role': 'pt'}
    )
    member_package = models.ForeignKey(
        MemberPackage,
        on_delete=models.RESTRICT,
        related_name='schedules',
        null=True,
        blank=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Kiểm tra số buổi còn lại nếu đặt lịch với PT
        if self.pt and self.member_package:
            if self.member_package.remaining_sessions <= 0:
                raise ValueError("No remaining PT sessions in this package.")
            if self.status == 'approved' and self._state.adding is False:  # Chỉ giảm khi cập nhật status thành approved
                if self.__class__.objects.get(pk=self.pk).status != 'approved':  # Kiểm tra status trước đó
                    self.member_package.remaining_sessions -= 1
                    self.member_package.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.start_time}"

    class Meta:
        ordering = ['start_time']