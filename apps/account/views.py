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




# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name", None)
#         password = request.POST.get("password")
#         password2 = request.POST.get("password2")

#         user = User.objects.filter(username=username).first()
#         if user:
#             messages.error(request, "User already exists!")
#             return redirect('register')
#         else:
#             if password != password2:
#                 messages.error(request, "Password did not match!")
#                 return redirect("register")
            
#             instance = User.objects.create_user(
#                                     username=username,
#                                     first_name=first_name, 
#                                     last_name=last_name,
#                                     password=password
#                                 )
            
#             user = authenticate(username=username, password=password)    
#             login(request, user)
#             messages.success(request, "Successfully created user!")
#             return redirect('/')
        
#     return render(request, 'auth/register.html')



