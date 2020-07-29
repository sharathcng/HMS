
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_page, name="homePage"),
    path('checkLogin/', views.check_login, name="checkLogin"),
    
]
