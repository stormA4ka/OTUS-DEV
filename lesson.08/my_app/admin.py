from django.contrib import admin
from my_app.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'phone_number', 'problem_description')
    fields = ('phone_number', 'problem_description', 'task_date')  # Укажите нужные поля