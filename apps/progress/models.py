from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User

class Progress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='progress_records',
        limit_choices_to={'role': 'member'}
    )
    pt = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pt_progress_records',
        null=True,
        blank=True,
        limit_choices_to={'role': 'pt'}
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(30), MaxValueValidator(150)]
    )
    body_fat = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    muscle_mass = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    note = models.TextField(null=True, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.recorded_at}"

    class Meta:
        ordering = ['recorded_at']