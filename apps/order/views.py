from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from apps.product.models import Product
from .models import ShopCart, Order, OrderItem, WishList
from apps.contact.models import Branch

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
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlists = WishList.objects.filter(user=request.user)
        else:
            wishlists = []

        context = {
            "wishlists": wishlists
        }
        return render(request, 'product/shop-wishlist.html', context)


class WishlistCreateView(View):
    def get(self, request, pk):
        url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, id=pk)
        user = request.user
        if WishList.objects.filter(user=user, product=product).exists():
            messages.error(request, "Bu mahsulot allaqachon bor!")
            return redirect(url)
        else:
            WishList.objects.create(
                user=user,
                product= product
            )
            messages.success(request, "Siz tanlagan maxsulot ro'yxatga qo'shildi!")
            return redirect(url)


def wishlist_delete(request, pk):
    wishlist = get_object_or_404(WishList, id=pk)
    wishlist.delete()
    return redirect("add_to_wishlist")


class ShopCartView(View):

    def get(self, request):
        branchs = Branch.objects.all()

        if request.user.is_authenticated:
            order_items = OrderItem.objects.filter(user=request.user, is_active=True)
            total_price = order_items.aggregate(Sum('price'))['price__sum']
        else:
            order_items = []
            total_price = 0

        context = {
            "order_items": order_items,
            "total_price": total_price,
            "branchs": branchs
        }
        return render(request, 'product/shop-cart.html', context)
    
    def post(self, request):
        url = request.META.get('HTTP_REFERER')

        name = request.POST.get('name')
        # email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        user = request.user
        if request.method == "POST":
            items = OrderItem.objects.filter(user=user, order=None)
            order = Order.objects.create(
                user=user,
                full_name=name,
                phone_number=phone, 
                status="PENDING",
                address=address
            )
            for i in items:
                i.order = order
                i.is_active = False
                i.save()
            messages.success(request, "Success")
            return redirect(url)
        
        return render(request, 'product/shop-cart.html')
                


def cart_item_delete(request, pk):
    item = get_object_or_404(OrderItem, id=pk)
    item.delete()
    return redirect("shop_cart")


def checkout(request):
    return render(request, 'product/shop-checkout.html')
