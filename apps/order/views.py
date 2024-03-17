from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from apps.product.models import Product
from .models import ShopCart, Order, OrderItem, WishList

from .forms import OrderForm
from django.contrib import messages


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
        result = int(quantity) * product.price
        cart.add_to_cart(product, quantity, result, color, size)
        return redirect('detail', product.slug)


class WishListView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        WishList.objects.get_or_create(user=request.user, product=product)
        return redirect('detail', product.slug)
    
    def get(self, request, *args, **kwargs):
        wishlists = WishList.objects.filter(user=request.user)
        context = {
            "wishlists": wishlists
        }
        return render(request, 'product/shop-wishlist.html', context)


def wishlist_delete(request, pk):
    wishlist = get_object_or_404(WishList, id=pk)
    print(wishlist, "########################################################")
    wishlist.delete()
    return redirect("add_to_wishlist")

