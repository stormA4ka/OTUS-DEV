from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Добро пожаловать!',
        'Спасибо за регистрацию на нашем сайте.',
        'noreply@example.com',
        [user_email],
        fail_silently=False,
    )