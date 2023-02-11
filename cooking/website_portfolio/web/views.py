from django.shortcuts import render
from .models import Web

def index(request):
    projects = Web.objects.all()
    return render(request, 'web/index.html', {'projects': projects})



