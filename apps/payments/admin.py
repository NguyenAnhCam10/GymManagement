from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member_package', 'amount', 'method', 'payment_date', 'status')
    list_filter = ('method', 'status')
    search_fields = ('member_package__user__username', 'member_package__package__name')
    date_hierarchy = 'payment_date'