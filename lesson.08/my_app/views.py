from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task  # Импортируем модель Task

def home(request):
    return render(request, 'my_app/home.html')

def task_list(request):
    tasks = Task.objects.all().order_by('-task_date')  # Получаем все заявки, сортируем по дате (новые сверху)
    return render(request, 'my_app/task_list.html', {'tasks': tasks})