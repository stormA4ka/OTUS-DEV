from django.contrib import admin
from .models import Task, Users

# Регистрация модели Users
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'first_name', 'last_name')  # Поля для отображения в списке
    list_filter = ('phone_number',)  # Фильтры
    search_fields = ('phone_number', 'first_name', 'last_name')  # Поля для поиска

# Регистрация модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'phone_number', 'problem_description', 'task_date')
    list_filter = ('task_date', 'problem_type')
    search_fields = ('problem_description', 'legal_entity', 'problem_location')

    # Кастомное действие для изменения описания проблемы
    @admin.action(description='Изменить описание проблемы')
    def update_problem_description(self, request, queryset):
        new_description = "Обновленное описание проблемы"  # Новое значение
        queryset.update(problem_description=new_description)
        self.message_user(request, f"Описание проблемы изменено для {queryset.count()} заявок.")

    # Добавляем действие в список доступных
    actions = [update_problem_description]

# Полная кастомизация
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('task_id', 'phone_number', 'problem_description', 'legal_entity', 'problem_type', 'task_date')
#     list_filter = ('task_date', 'problem_type', 'legal_entity')
#     search_fields = ('task_id', 'problem_description', 'legal_entity', 'problem_location')

#     # Кастомное действие для изменения описания проблемы
#     @admin.action(description='Изменить описание проблемы')
#     def update_problem_description(self, request, queryset):
#         new_description = "Обновленное описание проблемы"  # Новое значение
#         queryset.update(problem_description=new_description)
#         self.message_user(request, f"Описание проблемы изменено для {queryset.count()} заявок.")

#     # Кастомное действие для изменения типа проблемы
#     @admin.action(description='Изменить тип проблемы')
#     def update_problem_type(self, request, queryset):
#         new_type = "Обновленный тип проблемы"  # Новое значение
#         queryset.update(problem_type=new_type)
#         self.message_user(request, f"Тип проблемы изменен для {queryset.count()} заявок.")

#     # Добавляем действия в список доступных
#     actions = [update_problem_description, update_problem_type]
    