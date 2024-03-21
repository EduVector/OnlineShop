from django.db.models import Q
from django.contrib import messages
from apps.contact.models import GetInTouch
from .models import Category, Brand, Product
from apps.order.models import OrderItem, ShopCart, WishList, Order
from django.core.paginator import Paginator




def get_processors(request):
    q = request.GET.get('q')
    email = request.GET.get('getouch')
    page = request.GET.get('page', 1)


    categories = Category.objects.all()
    parent_cats = Category.objects.filter(level=0)
    brands = Brand.objects.all()
    products = Product.objects.filter(is_active=True).order_by("?")


    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(categories__name__icontains=q)
        )
    
    if email:
        GetInTouch.objects.create(email=email, full_name="From Subscribe")
        messages.success(request, "Successfully subscribed")

    
    if page:
        paginator = Paginator(products, 1)
        selected_page = paginator.get_page(page)

    wishlist = []
    shop_cart = []
    order_item = []

    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
        order_item = OrderItem.objects.filter(cart__user=request.user)
        shop_cart = ShopCart.objects.filter(user=request.user, is_complated=False)

    


    context = {
        "brands": brands,
        "categories": categories,
        "products": selected_page,
        "parent_cats": parent_cats,

        "order_item": order_item,
        "shop_cart": shop_cart,
        "wishlist": wishlist,
    }

    return context