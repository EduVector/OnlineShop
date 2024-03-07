from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Brand, Color, Product, ProductImage, AdditionalInfo, Rate, Tag, Size



@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    search_fields = ('id',  'name' )
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active', 'id')
    list_display_links = ('indented_title', 'id')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display =('name','created_at','id',)
    search_fields =('name', 'id')
    list_display_links =('name', 'id')

    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display =('name','color',)
    search_fields =('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','status','brand','views','id')
    search_fields =('name','status','categories')
    list_display_links =('name','status','brand','views','id')
    filter_horizontal = ('categories',)

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display =('product','key','value','id')
    list_display_links=('product','key','value','id')
    search_fields =('product', 'id')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product' , 'is_active' , 'created_at' , 'id')
    list_display_links  = ('product' , 'is_active' , 'created_at' , 'id')
    search_fields = ('product' , 'id')

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('user' , 'rate' , 'product'  , 'created_at')
    list_display_links  = ('user' , 'rate' , 'product'  , 'created_at')
    search_fields = ('product' , 'id' , 'user')
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name'  , 'created_at')
    list_display_links  = ('name' , 'created_at')
    search_fields = ('name' , 'id')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name'  , 'created_at')
    list_display_links  = ('name' , 'created_at')
    search_fields = ('name' , 'id')
