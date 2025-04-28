from django.contrib import admin
from .models import Progress

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'pt', 'weight', 'body_fat', 'muscle_mass', 'recorded_at')
    list_filter = ('pt',)
    search_fields = ('user__username', 'pt__username', 'note')
    date_hierarchy = 'recorded_at'