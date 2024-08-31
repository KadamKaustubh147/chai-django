from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, you are at the Home page")
    return render(request, "website/index.html") # request as a input leni hi padegi iss function ke liye.

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return HttpResponse("Hello world, you are at the contact  page")
