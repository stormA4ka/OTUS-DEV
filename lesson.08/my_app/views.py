from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task  # Импортируем модель Task
from .forms import TaskForm

def home(request):
    return render(request, 'my_app/home.html')

def task_list(request):
    tasks = Task.objects.all().order_by('-task_date')  # Получаем все заявки, сортируем по дате (новые сверху)
    return render(request, 'my_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'my_app/add_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Перенаправление на страницу списка заявок
    else:
        form = TaskForm(instance=task)
    return render(request, 'my_app/edit_task.html', {'form': form})

def about(request):
    return render(request, 'my_app/about.html')  # Укажите правильный путь к шаблону