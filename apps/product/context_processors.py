from django.db.models import Q
from django.contrib import messages
from apps.contact.models import GetInTouch
from .models import Category, Brand, Product
from apps.order.models import ShopCart, WishList, Order
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

    if request.user.is_authenticated:
        wishlist_count = WishList.objects.filter(user_id=request.user.id).count()
        carts = ShopCart.objects.filter(user=request.user.id, is_complated=False)


    context = {
        "brands": brands,
        "products": selected_page,
        "categories": categories,
        "parent_cats": parent_cats,
        "wishlist_count": wishlist_count,
        # "cart_items": carts.cart_items.all(),
        "cart_count": carts.count(),
    }

    return context