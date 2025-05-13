from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, MemberProfile

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),  # Loại bỏ created_at và last_login
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'role'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    # Đặt role mặc định là member khi tạo user mới
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Khi thêm user mới
            form.base_fields['role'].initial = 'member'  # Mặc định role là member
        return form

class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'bmi', 'updated_at')
    search_fields = ('user__username', 'user__email')
    exclude = ('bmi', 'updated_at')  # Loại bỏ bmi và updated_at khỏi form



    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(role='member')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(User, UserAdmin)
admin.site.register(MemberProfile, MemberProfileAdmin)

