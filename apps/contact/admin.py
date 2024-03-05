from django.contrib import admin
from .models import GetInTouch, Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display =('name','phone_number','address','location')
    list_display_links =('name','phone_number','address','location')
    search_fields =('name','address')


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display =('full_name','phone_number','email','message')
    list_display_links =('full_name','phone_number','email','message')
    search_fields  =('full_name','phone_number')