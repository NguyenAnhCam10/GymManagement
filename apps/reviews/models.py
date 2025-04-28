from django.db import models
from apps.users.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    pt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pt_reviews', null=True, blank=True)
    gym_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    pt_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"