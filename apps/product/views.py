from django.shortcuts import render
from django.views import View
from apps.product.models import (
    Category,
    Brand,
    Size,
    Tag,
    Product,
    ProductImage,
    Color,
    AdditionalInfo,
    Rate,
)
class HomePage(View):
    def get(self,request):
        products = Product.objects.filter(is_active=True,).order_by('?')[:16]
        popular_products = Product.objects.filter(is_active=True,).order_by('-views')[:16]
        new_products = Product.objects.filter(is_active=True,).order_by('-created_at')[:16]
        parent_cats = Category.objects.filter(level=0).order_by('?')

        ctx = {
            'products':products,
            'popular_products':popular_products,
            'new_products':new_products,
            'parent_cats':parent_cats,        
        }
        
        return render(request,'product/index.html',ctx)

def page404(request):
    return render(request,'product/page-404.html',{})

def page_about(request):
    return render(request,'product/page-about.html',{})

def shop_card(request):
    return render(request,'product/shop-cart.html',{})

def shop_checkout(request):
    return render(request,'product/shop-checkout.html',{})

def shop_filter(request):
    return render(request,'product/shop-filter.html',{})

def shop_grid(request):
    return render(request,'product/shop-grid-left.html',{})

def shop_product(request):
    return render(request,'product/shop-product-right.html',{})

def shop_wishlist(request):
    return render(request,'product/shop-wishlist.html',{})
