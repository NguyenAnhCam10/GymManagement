from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('pt', 'Personal Trainer'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='member')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    # Thêm related_name để tránh xung đột
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Đổi tên reverse accessor
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Đổi tên reverse accessor
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    # Thêm REQUIRED_FIELDS để yêu cầu nhập khi tạo superuser
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone', 'role']
    def __str__(self):
        return self.username

from decimal import Decimal

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # cm
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # kg
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goal = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_bmi(self):
        if self.height and self.weight and self.height > 0:  # Đảm bảo height > 0
            height_m = Decimal(self.height) / Decimal('100')  # Chuyển cm thành m
            bmi = Decimal(self.weight) / (height_m ** 2)
            return round(bmi, 2)
        return None

    def save(self, *args, **kwargs):
        self.bmi = self.calculate_bmi()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Profile of {self.user.username}"
