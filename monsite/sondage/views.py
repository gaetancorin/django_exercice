from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Citizen
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from scapy.all import *
from scapy.config import conf
# Create your views here.

from django.template import loader

def index(request):
    # listProtos=[layer.__name__ for layer in conf.layers]
    p = sniff(1, filter = "ip", iface="enp0s8")
    # context = {'allProtos': listProtos}
    context = {'packet': p[0][IP]}
    return render(request, 'sondage/index.html', context)

def my_login(request):
    return render(request, 'sondage/login.html')

def register(request):
    return render(request, 'sondage/register.html')

def my_logout(request):
    logout(request)
    return render(request, 'sondage/logout.html')

def registered(request):
    name= request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    citizen = Citizen(user=user)
    user.last_name = name
    user.first_name = firstname
    user.save()
    citizen.save()
    context = {'user':user}
    return render(request, 'sondage/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None:
        login(request, user)
        return render(request, 'sondage/welcome.html', context)
    else:
        return render(request, 'sondage/error_log.html')

def my_logout(request):
    logout(request)
    return render(request, 'sondage/logout.html')

def profil(request):
    citizen = Citizen.objects.get(user=request.user)
    context = {'citizen':citizen}
    return render(request, 'sondage/profil.html', context)

def become(request):
    request.user.citizen.electeur =True
    request.user.citizen.save()
    return IndexView.as_view()(request)
