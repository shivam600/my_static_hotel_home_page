from django.contrib import admin
from django.urls import path 

from . import views

urlpatterns = [
    path("" , views.my_home_page , name= "home"),
]
