from django.shortcuts import render, redirect
from .models import Web
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    projects = Web.objects.all()
    return render(request, 'web/index.html', {'projects': projects})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'web/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'web/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для ввода'})
        else:
            login(request, user)
            return redirect('currentweb')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'web/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentweb')
            except IntegrityError:
                return render(request, 'web/signupuser.html', {'form': UserCreationForm(),
                                                               'error': 'Такое имя пользователя уже существует. Задайте новое.'})
        else:
            return render(request, 'web/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают.'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def currentweb(request):
    return render(request, 'web/currentweb.html')
