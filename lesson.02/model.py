import datetime
import json
import os
import logging

# Настройка логгера
logging.basicConfig(filename='logs.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BookException(Exception):
    pass

class WrongInt(BookException):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Упсс.. Ожидалось целое число, но получено: {value}, введите данные корректно :)")

class User:
    _id_counter = 0

    def __init__(self, full_name, phone, comment, id=None, date_added=None):
        self.full_name = full_name
        self.phone = phone
        self.comment = comment
        self.id = id if id is not None else User._id_counter
        User._id_counter = self.id + 1 if id is None else User._id_counter
        self.date_added = date_added if date_added is not None else datetime.datetime.now()
        try:
            self.validate_int(phone)  # Проверка номера телефона
        except WrongInt as e:
            logging.error(f"Ошибка валидации номера телефона: {e}")
            raise

    def validate_int(self, value):
        try:
            int(value)
        except ValueError:
            raise WrongInt(value)

    def __str__(self):
        return (f"ID: {self.id}, ФИО: {self.full_name}, Телефон: {self.phone}, "
                f"Комментарий: {self.comment}, Дата добавления: {self.date_added}")

    @staticmethod
    def log_exceptions(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Ошибка в методе {func.__name__}: {e}")
                raise
        return wrapper

class Book(User):
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.read_users()

    @User.log_exceptions
    def read_users(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            User._id_counter = max([user['id'] for user in data], default=-1) + 1
            return [User(**user) for user in data]

    @User.log_exceptions
    def save_book(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([user.__dict__ for user in self.users], file, ensure_ascii=False, default=str)

    @User.log_exceptions
    def search_user(self, user_id):
        self.validate_int(user_id)
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    @User.log_exceptions
    def remove_user(self, user_id):
        self.validate_int(user_id)
        self.users = [user for user in self.users if user.id != user_id]
        self.save_book()

    @User.log_exceptions
    def edit_user(self, user_id, full_name=None, phone=None, comment=None):
        self.validate_int(user_id)
        user = self.search_user(user_id)
        if user:
            if full_name:
                user.full_name = full_name
            if phone:
                user.validate_int(phone)  # Проверка номера телефона
                user.phone = phone
            if comment:
                user.comment = comment
            self.save_book()

    @User.log_exceptions
    def add_user(self, full_name, phone, comment):
        new_user = User(full_name, phone, comment)
        self.users.append(new_user)
        self.save_book()
        return new_user

    @User.log_exceptions
    def reed_book(self):
        return self.read_users()

    @User.log_exceptions
    def about_book(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            record_count = len(data)
            file_size = os.path.getsize(self.file_path)
            return record_count, file_size