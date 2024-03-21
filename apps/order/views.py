from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from apps.product.models import Product
from .models import ShopCart, Order, OrderItem, WishList

from .forms import OrderForm
from django.contrib import messages
from django.db.models import Sum


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        color = request.POST.get('color')
        size = request.POST.get('size')

        product = get_object_or_404(Product, id=product_id)
        if product.colors.filter(name=color).exists() and not color:
            messages.error(request, "This color is not available")
        
        if product.sizes.filter(name=size).exists() and not size:
            messages.error(request, "This size is not available")

        cart, created = ShopCart.objects.get_or_create(user=request.user, is_complated=False)
        result = int(quantity) * product.get_new_price
        cart.add_to_cart(product, quantity, result, request.user)
        return redirect('detail', product.slug)


class WishListView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        WishList.objects.get_or_create(user=request.user, product=product)
        return redirect('detail', product.slug)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlists = WishList.objects.filter(user=request.user)
        else:
            wishlists = []

        context = {
            "wishlists": wishlists
        }
        return render(request, 'product/shop-wishlist.html', context)


def wishlist_delete(request, pk):
    wishlist = get_object_or_404(WishList, id=pk)
    wishlist.delete()
    return redirect("add_to_wishlist")


class ShopCartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            order_items = OrderItem.objects.filter(user=request.user)
            total_price = order_items.aggregate(Sum('price'))['price__sum']
        else:
            order_items = []
            total_price = 0

        context = {
            "order_items": order_items,
            "total_price": total_price
        }
        return render(request, 'product/shop-cart.html', context)


def cart_item_delete(request, pk):
    item = get_object_or_404(OrderItem, id=pk)
    item.delete()
    return redirect("shop_cart")


def checkout(request):
    return render(request, 'product/shop-checkout.html')
