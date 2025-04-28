from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'pt', 'start_time', 'end_time', 'status', 'note')
    list_filter = ('status', 'pt')
    search_fields = ('user__username', 'pt__username', 'note')
    date_hierarchy = 'start_time'