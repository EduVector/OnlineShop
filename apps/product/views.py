from django.shortcuts import render
from django.views import View
from apps.product.models import (
    Rate,
    Size, 
    Color,
    Product,
    Category, 
    ProductImage, 
)


class HomePage(View):
    def get(self, request):
        products = Product.objects.filter(is_active=True).order_by('?')
        popular_products = Product.objects.filter(is_active=True).order_by('-views')
        new_products = Product.objects.filter(is_active=True).order_by('-created_at')
        parent_cats = Category.objects.filter(level=0).order_by('?')

        top_sales = Product.objects.filter(status='SALE').order_by('?')
        top_rates = Product.objects.all().order_by('-product_rates__rate')


        context = {
            'products': products[:16],
            'new_products': new_products[:16],
            'parent_cats': parent_cats[:5],
            'popular_products': popular_products[:16],
            'new_arrivals': products[:20],
            'top_views': popular_products[:3],
            'top_sales': top_sales[:3],
            'top_rates': top_rates[:3]

        }
        return render(request, 'product/index.html', context)


class ShopView(View):
    def get(self, request):
        return render(request, 'product/shop.html')