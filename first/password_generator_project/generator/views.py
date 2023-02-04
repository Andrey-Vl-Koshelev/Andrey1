from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})

def password(request):
    char = [chr(i) for i in range(97, 123)]
    nul = [chr(i) for i in range(48, 58)]
    dec = [chr(i) for i in range(33, 48)]
    upp = [i.upper() for i in char]
    length = int(request.GET.get('length'))
    special = request.GET.get('special')
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    psw = ''
    for i in range(length):
        if numbers:
            psw += random.choice(nul)
        elif uppercase:
            psw += random.choice(upp)
        elif special :
            psw += random.choice(dec)
        else:
            psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})
