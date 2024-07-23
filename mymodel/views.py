from django.conf import settings
from django.shortcuts import render
import os

def home(request):
    for directory in settings.template[0]['DIRS']:
        print(f"template directory: {directory}")
    return render(request, 'myapp/home.html')


