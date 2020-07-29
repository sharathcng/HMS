from django.shortcuts import render,redirect,reverse

# Create your views here.


def home_page(request):
    return render(request,'hospital/homePage.html')


def check_login(request):
    return render(request,'hospital/checkLogin.html')

