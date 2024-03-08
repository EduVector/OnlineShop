from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.views import generic, View


class RegisterView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class
        ctx = {
            "form": form
        }
        return render(request, 'auth/register.html', ctx)
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        messages.error(request, f"{form.errors}")
        ctx = {
            "form": form
        }
        return render(request, 'auth/register.html', ctx)
        

class LoginView(View):
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = self.form_class
        return render(request, 'auth/login.html', {"form": form})

    def post(self, request):
        url = request.META.get("HTTP_PREFERER")
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("/")
        
        return render(request, 'auth/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out.")
        return redirect("/")
