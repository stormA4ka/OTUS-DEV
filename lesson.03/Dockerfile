# Dockerfile для FastAPI приложения
# Для сборки образа выполните:
# docker build -t myfastapiapp .
# Для запуска контейнера выполните:
# docker run -d -p 8000:8000 myfastapiapp

# Используем базовый образ Python 3.9 slim
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы и папки приложения в рабочую директорию
COPY . .

# Указываем порт, который будет использоваться приложением
EXPOSE 8000

# Запускаем веб-сервер Uvicorn с параметрами host 0.0.0.0 и port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]