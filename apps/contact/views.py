from django.shortcuts import render

def contact(request):
    return render(request,'contact/page-contact.html',{})

# Create your views here.
