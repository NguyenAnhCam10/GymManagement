from django.contrib import admin
from .models import Package, MemberPackage

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pt_sessions', 'duration', 'is_active', 'created_by')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(MemberPackage)
class MemberPackageAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'start_date', 'end_date', 'remaining_sessions', 'status')
    list_filter = ('status', 'package')
    search_fields = ('user__username', 'package__name')
