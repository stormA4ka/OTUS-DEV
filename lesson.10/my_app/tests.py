from django.test import TestCase
from django.urls import reverse
from .models import Task, Users

class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        cls.user = Users.objects.create(
            phone_number='12345678901',
            first_name='Иван',
            last_name='Иванов'
        )

        # Создаем тестовую задачу
        cls.task = Task.objects.create(
            phone_number=cls.user,
            platform_type='Тип площадки',
            legal_entity='ООО "Пример"',
            problem_description='Тестовая проблема',
            problem_location='Тестовое место',
            problem_type='Тестовый тип',
        )

    # Тест для создания задачи
    def test_task_creation(self):
        task = Task.objects.get(task_id=self.task.task_id)
        self.assertEqual(task.problem_description, 'Тестовая проблема')
        self.assertEqual(task.phone_number.phone_number, '12345678901')

    # Тест для чтения задачи
    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.task_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая проблема')

    # Тест для обновления задачи
    def test_task_update(self):
        response = self.client.post(
            reverse('task_update', args=[self.task.task_id]),
            {
                'phone_number': self.user.id,
                'platform_type': 'Обновленный тип площадки',
                'legal_entity': 'ООО "Обновленный"',
                'problem_description': 'Обновленная проблема',
                'problem_location': 'Обновленное место',
                'problem_type': 'Обновленный тип',
            }
        )
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление после успешного обновления
        updated_task = Task.objects.get(task_id=self.task.task_id)
        self.assertEqual(updated_task.problem_description, 'Обновленная проблема')

    # Тест для удаления задачи
    def test_task_delete(self):
        response = self.client.post(reverse('task_delete', args=[self.task.task_id]))
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление после успешного удаления
        self.assertFalse(Task.objects.filter(task_id=self.task.task_id).exists())