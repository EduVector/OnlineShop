from .models import Category, Brand, Product
from apps.order.models import ShopCart, WishList, Order
from django.db.models import Q


def get_processors(request):
    q = request.GET.get('q')

    categories = Category.objects.all()
    parent_cats = Category.objects.filter(level=0)
    brands = Brand.objects.all()
    products = Product.objects.all()

    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(categories__name__icontains=q)
        )


    context = {
        "brands": brands,
        "products": products,
        "categories": categories,
        "parent_cats": parent_cats,
    }

    return context