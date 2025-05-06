from django.db import models
from apps.users.models import User

class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        limit_choices_to={'role': 'member'}
    )
    pt = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pt_reviews',
        null=True,
        blank=True,
        limit_choices_to={'role': 'pt'}
    )
    gym_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    pt_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.pt and self.pt_rating is not None:
            raise ValueError("pt_rating should be null when there is no PT.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by {self.user.username}"