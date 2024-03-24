from django.urls import path
from .views import (
    AddToCartView,
    WishListView,
    wishlist_delete,
    ShopCartView,
    cart_item_delete,
    checkout,
    WishlistCreateView
)

# app_name = 'order'

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('wishlist/', WishListView.as_view(), name='add_to_wishlist'),
    path('wishlist-delete/<int:pk>/', wishlist_delete, name='wishlist_delete'),
    path('items/', ShopCartView.as_view(), name="shop_cart"),
    path('item/delete/<int:pk>/', cart_item_delete, name="delete_item"),
    path('check/', checkout),
    path('wish/<int:pk>/', WishlistCreateView.as_view(), name="product_wishlist")
]