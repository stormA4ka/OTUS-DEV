import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Создаём экземпляр Celery
app = Celery("config")

# Загружаем настройки из настроек Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически находим и регистрируем задачи в приложениях Django
app.autodiscover_tasks()

# Настройка для broker_connection_retry_on_startup
app.conf.broker_connection_retry_on_startup = True
