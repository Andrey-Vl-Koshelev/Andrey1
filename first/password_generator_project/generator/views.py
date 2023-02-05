from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    lst = list(range(10, 21))
    return render(request, 'generator/home.html', {'lst': lst})

def password(request):
    # char = [chr(i) for i in range(97, 123)]
    # nul = [chr(i) for i in range(48, 58)]
    # dec = [chr(i) for i in range(33, 48)]
    # upp = [i.upper() for i in char]
    # length = int(request.GET.get('length'))
    # special = request.GET.get('special')
    # uppercase = request.GET.get('uppercase')
    # numbers = request.GET.get('numbers')
    # psw = ''
    # for i in range(length):
    #     if numbers and uppercase and special:
    #         psw += (random.choice(char) + random.choice(nul) + random.choice(upp) + random.choice(dec))
    #     elif numbers and uppercase:
    #         psw += (random.choice(char) + random.choice(nul) + random.choice(upp))
    #     elif special and uppercase:
    #         psw += (random.choice(char) + random.choice(dec) + random.choice(upp))
    #     elif special and numbers:
    #         psw += (random.choice(char) + random.choice(dec) + random.choice(nul))
    #     elif uppercase:
    #         psw += (random.choice(char) + random.choice(upp))
    #     elif special:
    #         psw += (random.choice(char) + random.choice(dec))
    #     elif numbers:
    #         psw += (random.choice(char) + random.choice(nul))
    #     else:
    #         psw += random.choice(char)
    # res = ''.join(random.choices(psw, k=length))
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65,91)])
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48,58)])
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33,48)])

    length = int(request.GET.get('length'))
    psw = ''
    for i in range(length):
        psw += random.choice(char)

    return render(request, 'generator/password.html', {'password': psw})
