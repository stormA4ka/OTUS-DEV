from django.db import models
from django.utils import timezone

class Application(models.Model):
    # Обязательные поля
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    platform_type = models.CharField(max_length=100, verbose_name="Тип площадки")
    legal_entity = models.CharField(max_length=100, verbose_name="Юрлицо")
    problem_description = models.TextField(verbose_name="Краткое описание проблемы")
    problem_location = models.CharField(max_length=200, verbose_name="Место проблемы")
    problem_type = models.CharField(max_length=100, verbose_name="Тип проблемы")
    application_date = models.DateTimeField(default=timezone.now, verbose_name="Дата заявки")
    application_id = models.AutoField(primary_key=True, verbose_name="Номер заявки ID")

    # Необязательные поля
    problem_photo = models.ImageField(upload_to='problem_photos/', blank=True, null=True, verbose_name="Фото проблемы")
    solution_proposal = models.TextField(blank=True, null=True, verbose_name="Предложение по устранению")
    responsible_person = models.CharField(max_length=100, blank=True, null=True, verbose_name="ФИО (ответственного за устранение)")
    initiator_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="ФИО (инициатора)")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="Должность")
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отдел инициатора")
    planned_fix_date = models.DateField(blank=True, null=True, verbose_name="Плановая дата устранения")

    def __str__(self):
        return f"Заявка #{self.application_id}"