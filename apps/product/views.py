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
        products = Product.objects.filter(is_active=True).order_by('?')[:16]
        popular_products = Product.objects.filter(is_active=True).order_by('-views')[:16]
        new_products = Product.objects.filter(is_active=True).order_by('-created_at')[:16]
        parent_cats = Category.objects.filter(level=0).order_by('?')
        all_products = Product.objects.all()
        context = {
            'products': products,
            'new_products': new_products,
            'parent_cats': parent_cats[:5],
            'popular_products': popular_products,
            'all_products':all_products
        }
        return render(request, 'product/index.html', context)