# Generated by Django 5.1.4 on 2025-01-12 17:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('platform_type', models.CharField(max_length=100, verbose_name='Тип площадки')),
                ('legal_entity', models.CharField(max_length=100, verbose_name='Юрлицо')),
                ('problem_description', models.TextField(verbose_name='Краткое описание проблемы')),
                ('problem_location', models.CharField(max_length=200, verbose_name='Место проблемы')),
                ('problem_type', models.CharField(max_length=100, verbose_name='Тип проблемы')),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заявки')),
                ('application_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер заявки ID')),
                ('problem_photo', models.ImageField(blank=True, null=True, upload_to='problem_photos/', verbose_name='Фото проблемы')),
                ('solution_proposal', models.TextField(blank=True, null=True, verbose_name='Предложение по устранению')),
                ('responsible_person', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО (ответственного за устранение)')),
                ('initiator_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО (инициатора)')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отдел инициатора')),
                ('planned_fix_date', models.DateField(blank=True, null=True, verbose_name='Плановая дата устранения')),
            ],
        ),
    ]
