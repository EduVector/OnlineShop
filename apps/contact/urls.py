from django.urls import path
from .views import contact

urlpatterns = [
    path('contact/',contact,name = 'page-contact.html'),
]