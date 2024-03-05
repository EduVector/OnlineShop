from django.urls import path 
from .import views

urlpatterns = [
    path('page_contact/',views.contact, name='page-contact.html'),
]