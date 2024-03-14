from django.shortcuts import render, get_object_or_404
from django.views import View
from apps.product.models import (
    Tag,
    Rate,
    Size, 
    Color,
    Brand,
    Product,
    Category, 
    ProductImage, 
)

from django.core.paginator import Paginator


class HomePage(View):
    def get(self, request):
        products = Product.objects.filter(is_active=True).order_by('?')
        popular_products = Product.objects.filter(is_active=True).order_by('-views')
        new_products = Product.objects.filter(is_active=True).order_by('-created_at')
        parent_cats = Category.objects.filter(level=0).order_by('?')

        top_sales = Product.objects.filter(status='SALE').order_by('?')
        top_rates = Product.objects.all().order_by('-product_rates__rate')


        context = {
            'products': products[:16],
            'new_products': new_products[:16],
            'parent_cats': parent_cats[:5],
            'popular_products': popular_products[:16],
            'new_arrivals': products[:20],
            'top_views': popular_products[:3],
            'top_sales': top_sales[:3],
            'top_rates': top_rates[:3],
            'main_products': products[16:32]

        }
        return render(request, 'product/index.html', context)


class ShopView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        show = request.GET.get('show', 50)

        products = Product.objects.filter(is_active=True).order_by("?")
        new_products = Product.objects.filter(is_active=True).order_by('-id')
        categories = Category.objects.all()
        brands = Brand.objects.all()

        if page:
            paginator = Paginator(products, int(show))
            selected_page = paginator.get_page(page)


        context = {
            "brands": brands,
            "categories": categories,
            "products": selected_page,
            "new_products": new_products,
        }
        return render(request, 'product/shop.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)

        tags = product.tags.all()
        sizes = product.sizes.all()
        images = product.images.all()
        colors = product.colors.all()
        prod_categories = product.categories.all()
        additional_info = product.additional_info.all()
        



        context = {
            "tags": tags,
            "sizes": sizes,
            "images": images,
            "colors": colors,
            "product": product,
            "prod_categories": prod_categories,
            "additional_info": additional_info,
        }
        return render(request, 'product/shop-detail.html', context)