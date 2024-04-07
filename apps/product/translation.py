from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category


class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')


class CategoryTranslation(TranslationOptions):
    fields = ('name',)


translator.register(Product, ProductTranslation)
translator.register(Category, CategoryTranslation)
