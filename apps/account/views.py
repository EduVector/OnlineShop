from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request,"Ushbu foydalanuvchi ro'yhatdan o'tgan")
            return redirect('register')
        else:
            if password != password2:
                messages.error(request,'Birinchi parol bilan ikkinchi parol bir xil emas !!!!')
                return redirect('register')
            instance = User.objects.create_user(
                                username=username,
                                password=password,
                            )
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Tizimdan muvafaqiyatli ro'yxatdan o'tdingiz")
            return redirect('/')
    return render(request,'auth/register.html',{})
