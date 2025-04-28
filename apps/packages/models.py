from django.db import models
from apps.users.models import User

class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    pt_sessions = models.IntegerField(default=0)  # Số buổi với PT
    duration = models.IntegerField()  # Thời gian hiệu lực (ngày)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='created_packages')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MemberPackage(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member_packages')
    package = models.ForeignKey(Package, on_delete=models.RESTRICT, related_name='member_packages')
    start_date = models.DateField()
    end_date = models.DateField()
    remaining_sessions = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.user.username} - {self.package.name}"