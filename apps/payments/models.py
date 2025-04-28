from django.db import models
from apps.packages.models import MemberPackage

class Payment(models.Model):
    METHOD_CHOICES = (
        ('momo', 'MoMo'),
        ('vnpay', 'VNPAY'),
        ('bank', 'Bank Transfer'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    member_package = models.ForeignKey(MemberPackage, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    receipt_url = models.URLField(null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment {self.member_package} - {self.amount}"