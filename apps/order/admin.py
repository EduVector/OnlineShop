from django.contrib import admin
from .models import WishList, ShopCart, Order, OrderItem

# Register your models here.

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_complated', 'created_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user', 'phone_numeber', 'created_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'order', 'product', 'quantity', 'price', 'created_at']