from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'type', 'sent_at', 'is_read')
    list_filter = ('type', 'is_read')
    search_fields = ('title', 'message', 'user__username')
    date_hierarchy = 'sent_at'