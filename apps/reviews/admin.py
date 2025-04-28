from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'pt', 'gym_rating', 'pt_rating', 'created_at')
    list_filter = ('gym_rating', 'pt_rating')
    search_fields = ('user__username', 'pt__username', 'comment')
    date_hierarchy = 'created_at'