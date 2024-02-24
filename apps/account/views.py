from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name", None)
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, "User already exists!")
            return redirect('register')
        else:
            if password != password2:
                messages.error(request, "Password did not match!")
                return redirect("register")
            
            instance = User.objects.create_user(
                                    username=username,
                                    first_name=first_name, 
                                    last_name=last_name,
                                    password=password
                                )
            
            user = authenticate(username=username, password=password)    
            login(request, user)
            messages.success(request, "Successfully created user!")
            return redirect('/')
        
    return render(request, 'auth/register.html')






            