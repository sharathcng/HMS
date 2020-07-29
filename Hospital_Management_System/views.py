from django.shortcuts import render,redirect,reverse

def check_login(request):
    return render(request,'hospital/checkLogin.html')