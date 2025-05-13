from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'pt', 'start_time', 'end_time', 'status', 'note')
    list_filter = ('status', 'pt')
    search_fields = ('user__username', 'pt__username', 'note')
    date_hierarchy = 'start_time'
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'pt':
            return qs.filter(pt=request.user)  # PT chỉ thấy lịch của mình
        return qs

    def get_readonly_fields(self, request, obj=None):
        if request.user.role == 'pt':
            return ['user', 'member_package', 'created_at', 'updated_at']  # PT không sửa các trường này
        return []

    def has_add_permission(self, request):
        return True  # PT có thể tạo lịch mới

    def has_change_permission(self, request, obj=None):
        return True  # PT có thể sửa lịch

    def has_delete_permission(self, request, obj=None):
        if request.user.role == 'pt':
            return False  # PT không được xóa lịch
        return True