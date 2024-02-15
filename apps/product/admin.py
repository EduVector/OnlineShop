from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Brand, Color, Product, ProductImage, AdditionalInfo, Rate, Tag


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active', 'id')
    list_display_links = ('indented_title', 'id')
