from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('detail/', views.ProductDetailView.as_view(), name='detail'),
]




