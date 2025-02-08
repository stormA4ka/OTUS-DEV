import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from my_app.models import Users, Task
from django.utils import timezone

# Создание пользователей
user1 = Users.objects.create(
    phone_number="12345678901",
    first_name="Иван",
    last_name="Иванов"
)

user2 = Users.objects.create(
    phone_number="23456789012",
    first_name="Петр",
    last_name="Петров"
)

user3 = Users.objects.create(
    phone_number="34567890123",
    first_name="Анна",
    last_name="Антонова"
)

# Создание задач для пользователя 1
task1 = Task.objects.create(
    phone_number=user1,
    platform_type="Веб-сайт",
    legal_entity="ООО Ромашка",
    problem_description="Сайт не открывается",
    problem_location="Главная страница",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить хостинг",
    responsible_person="Петр Петров",
    initiator_name="Иван Иванов",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task2 = Task.objects.create(
    phone_number=user1,
    platform_type="Мобильное приложение",
    legal_entity="ООО Василек",
    problem_description="Приложение вылетает",
    problem_location="Экран входа",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить логи",
    responsible_person="Анна Антонова",
    initiator_name="Иван Иванов",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task3 = Task.objects.create(
    phone_number=user1,
    platform_type="Веб-сайт",
    legal_entity="ООО Ромашка",
    problem_description="Сайт медленно загружается",
    problem_location="Главная страница",
    problem_type="Производительность",
    task_date=timezone.now(),
    solution_proposal="Оптимизировать изображения",
    responsible_person="Петр Петров",
    initiator_name="Иван Иванов",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

# Создание задач для пользователя 2
task4 = Task.objects.create(
    phone_number=user2,
    platform_type="Веб-сайт",
    legal_entity="ООО Василек",
    problem_description="Сайт не открывается",
    problem_location="Главная страница",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить хостинг",
    responsible_person="Иван Иванов",
    initiator_name="Петр Петров",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task5 = Task.objects.create(
    phone_number=user2,
    platform_type="Мобильное приложение",
    legal_entity="ООО Ромашка",
    problem_description="Приложение вылетает",
    problem_location="Экран входа",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить логи",
    responsible_person="Анна Антонова",
    initiator_name="Петр Петров",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task6 = Task.objects.create(
    phone_number=user2,
    platform_type="Веб-сайт",
    legal_entity="ООО Василек",
    problem_description="Сайт медленно загружается",
    problem_location="Главная страница",
    problem_type="Производительность",
    task_date=timezone.now(),
    solution_proposal="Оптимизировать изображения",
    responsible_person="Иван Иванов",
    initiator_name="Петр Петров",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

# Создание задач для пользователя 3
task7 = Task.objects.create(
    phone_number=user3,
    platform_type="Веб-сайт",
    legal_entity="ООО Ромашка",
    problem_description="Сайт не открывается",
    problem_location="Главная страница",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить хостинг",
    responsible_person="Петр Петров",
    initiator_name="Анна Антонова",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task8 = Task.objects.create(
    phone_number=user3,
    platform_type="Мобильное приложение",
    legal_entity="ООО Василек",
    problem_description="Приложение вылетает",
    problem_location="Экран входа",
    problem_type="Техническая проблема",
    task_date=timezone.now(),
    solution_proposal="Проверить логи",
    responsible_person="Иван Иванов",
    initiator_name="Анна Антонова",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)

task9 = Task.objects.create(
    phone_number=user3,
    platform_type="Веб-сайт",
    legal_entity="ООО Ромашка",
    problem_description="Сайт медленно загружается",
    problem_location="Главная страница",
    problem_type="Производительность",
    task_date=timezone.now(),
    solution_proposal="Оптимизировать изображения",
    responsible_person="Петр Петров",
    initiator_name="Анна Антонова",
    position="Менеджер",
    department="IT",
    planned_fix_date=timezone.now().date()
)
