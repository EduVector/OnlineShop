from django.db.models import Q
from django.contrib import messages
from apps.contact.models import GetInTouch
from .models import Category, Brand, Product
from apps.order.models import ShopCart, WishList, Order



def get_processors(request):
    q = request.GET.get('q')
    email = request.GET.get('getouch')

    categories = Category.objects.all()
    parent_cats = Category.objects.filter(level=0)
    brands = Brand.objects.all()
    products = Product.objects.all()

    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(categories__name__icontains=q)
        )
    
    if email:
        GetInTouch.objects.create(email=email, full_name="From Subscribe")
        messages.success(request, "Successfully subscribed")


    context = {
        "brands": brands,
        "products": products,
        "categories": categories,
        "parent_cats": parent_cats,
    }

    return context