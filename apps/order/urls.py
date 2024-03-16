from django.urls import path
from .views import (
    AddToCartView,
    WishListView,
    wishlist_delete,
)

# app_name = 'order'

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('wishlist/', WishListView.as_view(), name='add_to_wishlist'),
    path('wishlist-delete/<int:pk>/', wishlist_delete, name='wishlist_delete')   
]