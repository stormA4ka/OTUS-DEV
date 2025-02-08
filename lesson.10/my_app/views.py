# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task, Users, Log  # Импортируем модель Task и Log
from .forms import TaskForm, UsersForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .tasks import log_task_action
from openpyxl import Workbook

def home(request):
    return render(request, 'my_app/home.html')

def task_list(request):
    tasks = Task.objects.all().order_by('-task_date')  # Получаем все заявки, сортируем по дате (новые сверху)
    return render(request, 'my_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            log_task_action.delay('Создание', task.task_id)  # Логирование создания задачи
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
            log_task_action.delay('Редактирование', task.task_id)  # Логирование редактирования задачи
            return redirect('task_list')  # Перенаправление на страницу списка заявок
    else:
        form = TaskForm(instance=task)
    return render(request, 'my_app/edit_task.html', {'form': form})

def about(request):
    return render(request, 'my_app/about.html')  # Укажите правильный путь к шаблону

def user_list(request):
    users = Users.objects.all()  # Получаем всех пользователей из базы данных
    return render(request, 'my_app/users_list.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')  # Перенаправление на страницу списка пользователей
    else:
        form = UsersForm()
    return render(request, 'my_app/add_user.html', {'form': form})

def edit_user(request, user_id):
    user = Users.objects.get(id=user_id)
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_list')  # Перенаправление на страницу списка пользователей
    else:
        form = UsersForm(instance=user)
    return render(request, 'my_app/edit_user.html', {'form': form})

class TaskListView(ListView):
    model = Task  # Указываем модель
    template_name = 'my_app/task_list.html'  # Шаблон для отображения
    context_object_name = 'tasks'  # Имя переменной в шаблоне
    ordering = ['-task_date']  # Сортировка по дате (новые сверху)

class TaskDetailView(DetailView):
    model = Task  # Указываем модель
    template_name = 'my_app/task_detail.html'  # Шаблон для отображения
    context_object_name = 'task'  # Имя переменной в шаблоне
    pk_url_kwarg = 'task_id'  # Имя параметра в URL

class TaskCreateView(CreateView):
    model = Task  # Указываем модель
    form_class = TaskForm  # Указываем форму
    template_name = 'my_app/task_form.html'  # Шаблон для отображения
    success_url = '/tasks/'  # URL для перенаправления после успешного создания

    def form_valid(self, form):
        response = super().form_valid(form)
        log_task_action.delay('Создание', self.object.task_id)  # Логирование создания задачи
        return response

class TaskUpdateView(UpdateView):
    model = Task  # Указываем модель
    form_class = TaskForm  # Указываем форму
    template_name = 'my_app/task_form.html'  # Шаблон для отображения
    pk_url_kwarg = 'task_id'  # Имя параметра в URL
    success_url = '/tasks/'  # URL для перенаправления после успешного редактирования

    def form_valid(self, form):
        response = super().form_valid(form)
        log_task_action.delay('Редактирование', self.object.task_id)  # Логирование редактирования задачи
        return response

class TaskDeleteView(DeleteView):
    model = Task  # Указываем модель
    template_name = 'my_app/task_confirm_delete.html'  # Шаблон для подтверждения удаления
    pk_url_kwarg = 'task_id'  # Имя параметра в URL
    success_url = '/tasks/'  # URL для перенаправления после успешного удаления

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        log_task_action.delay('Удаление', self.object.task_id)  # Логирование удаления задачи
        return response

def register_user(request):
    # Логика регистрации пользователя
    user_email = request.POST['email']
    send_welcome_email.delay(user_email)  # Отправка задачи в Celery
    return HttpResponse("Регистрация завершена. Проверьте ваш email.")

def generate_report(request):
    tasks = Task.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.title = "Tasks Report"

    # Заголовки
    ws.append(['Номер заявки', 'Номер телефона', 'Тип площадки', 'Юрлицо', 'Описание проблемы', 'Место проблемы', 'Тип проблемы', 'Дата заявки'])

    # Данные
    for task in tasks:
        ws.append([
            task.task_id,
            task.phone_number.phone_number,
            task.platform_type,
            task.legal_entity,
            task.problem_description,
            task.problem_location,
            task.problem_type,
            task.task_date.replace(tzinfo=None)  # Удаление информации о временной зоне
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=tasks_report.xlsx'
    wb.save(response)
    return response