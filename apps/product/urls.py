from django.urls import path
from . import views

# app_name = 'product'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/detail/<str:slug>/', views.ProductDetailView.as_view(), name='detail'),
]
