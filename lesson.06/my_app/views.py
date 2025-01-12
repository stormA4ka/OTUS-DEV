from django.shortcuts import render, redirect
from .models import Application
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")