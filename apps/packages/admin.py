from django.contrib import admin
from .models import Package, MemberPackage

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'pt_sessions', 'package_type', 'is_active']  # Xóa 'duration'
    list_filter = ['package_type', 'is_active']
    search_fields = ['name']

@admin.register(MemberPackage)
class MemberPackageAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'start_date', 'end_date', 'status']
    list_filter = ['status']
    search_fields = ['user__username', 'package__name']