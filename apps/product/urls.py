from django.urls import path
from .import views

urlpatterns = [
    path('',views.HomePage.as_view(), name="index.html"),
    path('page404/',views.page404, name='page-404.html'),
    path('page_about/',views.page_about, name='page_about.html'),
    path('shop_card/',views.shop_card, name='shop_cart.html'),
    path('shop_checkout/',views.shop_checkout, name='shop-checkout.html'),
    path('shop_filter/',views.shop_filter,name='shop-filter.html'),
    path('shop_grid/',views.shop_grid, name='shop-grid.html'),
    path('shop_product/',views.shop_product, name='shop-product-right.html'),
    path('shop_wishlist/',views.shop_wishlist, name='shop-wishlist.html'),
]