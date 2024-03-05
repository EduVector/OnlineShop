from django.shortcuts import render
from 

def index(request):
    return render(request,'product/index.html',{})

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
