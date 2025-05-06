from django.db import models
from apps.users.models import User
from django.core.validators import MinValueValidator
class Package(models.Model):
    PACKAGE_TYPE_CHOICES = (
        ('monthly', 'Monthly'),  # Tháng
        ('quarterly', 'Quarterly'),  # Quý
        ('yearly', 'Yearly'),  # Năm
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    pt_sessions = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Số buổi với PT
    package_type = models.CharField(max_length=10, choices=PACKAGE_TYPE_CHOICES, default='monthly')  # Thêm default, quý, năm
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='created_packages')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
from datetime import datetime, timedelta

class MemberPackage(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member_packages', limit_choices_to={'role': 'member'})
    package = models.ForeignKey(Package, on_delete=models.RESTRICT, related_name='member_packages')
    start_date = models.DateField()
    end_date = models.DateField()
    remaining_sessions = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Tự động tính end_date khi tạo mới
        if not self.id:  # Chỉ tính khi tạo mới
            if self.package.package_type == 'monthly':
                self.end_date = self.start_date + timedelta(days=30)  # 1 tháng = 30 ngày
            elif self.package.package_type == 'quarterly':
                self.end_date = self.start_date + timedelta(days=90)  # 1 quý = 90 ngày
            elif self.package.package_type == 'yearly':
                self.end_date = self.start_date + timedelta(days=365)  # 1 năm = 365 ngày

            # Gán remaining_sessions
            self.remaining_sessions = self.package.pt_sessions

        # Tự động cập nhật status
        if self.end_date < datetime.now().date():
            self.status = 'expired'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.package.name}"