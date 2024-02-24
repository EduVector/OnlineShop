from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Brand, Color, Product, ProductImage, AdditionalInfo, Rate, Tag, Size


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active', 'id')
    list_display_links = ('indented_title', 'id')
    search_fields = ('name', 'id')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display =('name','created_at','id',)
    search_fields =('name', 'id')
    list_display_links =('name', 'id')

    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display =('name','color','id')
    search_fields =('name','id')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','status','brand','views','id')
    search_fields =('name','status','categories')
    list_display_links =('name','status','brand','views','id')
    filter_horizontal =('categories',)
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display =('product','is_active', 'created_at','id')
    list_display_links =('product','is_active', 'created_at','id')
    search_fields =('product','id')

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display =('product','key','value','id')
    list_display_links=('product','key','value','id')
    search_fields =('product', 'id')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =('name','id')
    list_display_links=('name','id')
    search_fields =('name',)

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display =('product','rate','user',)
    list_display_links =('product','rate','user',)
    search_fields =('product','user',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display =('name','created_at','id',)
    list_display_links =('name','created_at','id',)
    search_fields =('name',)