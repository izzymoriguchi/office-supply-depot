from django.contrib import admin
from .models import Order, OrderDetail

# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderDetail
    fieldsets = [
    ('Product',{'fields':['product']}),
    ('Quantity',{'fields':['quantity']}),
    ('Price',{'fields':['price']}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0
    template = 'admin/order/tabular.html'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'ship_address', 'order_date']
    list_display_links = ['order_id']
    search_fields = ['order_id', 'ship_address']
    readonly_fields = ['order_id', 'total', 'ship_address', 'order_date', 'total']
    fieldsets = [
        ('ORDER INFORMATION',{'fields':['order_id', 'order_date']}),
        ('BILLING INFORMATION',{'fields':['total']}),
        ('SHIPPING INFORMATION',{'fields':['ship_address']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
