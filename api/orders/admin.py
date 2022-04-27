from django.contrib import admin
from orders.models import Order, OrderItem
# Register your models here.


class OrderItemTabuler(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_name_fields = ['product', ]

# admin.site.register(OrderItem)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price',
                    'status']
    list_filter = ['status']
    raw_user_fields = ['user']
    list_editable = ['status']
    inlines = [OrderItemTabuler]
    list_per_page = 24