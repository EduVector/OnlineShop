from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import WishList,ShopCart,Order,OrderItem

# Register your models here.

@admin.register(WishList)
class WishList(DraggableMPTTAdmin):
    mptt_indent_field = "name"

@admin.register(ShopCart)
class AdminShopCart(DraggableMPTTAdmin):
    mptt_indent_field = "name"

@admin.register(Order)
class AdminOrder(DraggableMPTTAdmin):
    mptt_indent_field = "name"

@admin.register(OrderItem)
class AdminOrderItem(DraggableMPTTAdmin):
    mptt_indent_field = "name"