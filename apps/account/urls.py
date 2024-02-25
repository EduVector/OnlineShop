from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('sing_in/' , views.sing_in , name='sing_in')
]
