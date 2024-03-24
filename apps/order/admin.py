from django.contrib import admin
from .models import WishList, ShopCart, Order, OrderItem

# Register your models here.

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_complated', 'created_at')


class OrderItemInline(admin.StackedInline):
    readonly_fields = ['product', 'user', 'cart', 'quantity', 'is_active', 'price']
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'status', 'user', 'phone_number', 'created_at']
    list_filter = ['status']
    date_hierarchy = 'created_at'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'order', 'product', 'quantity', 'price', 'created_at']