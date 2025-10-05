from django.shortcuts import render

import requests
# Create your views here.


def my_home_page(request):
    return render(request , 'index.html')