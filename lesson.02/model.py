import datetime
import json
import os


import datetime

class User:
    _id_counter = 0

    def __init__(self, full_name, phone, comment, id=None, date_added=None):
        self.full_name = full_name
        self.phone = phone
        self.comment = comment
        self.id = id if id is not None else User._id_counter
        User._id_counter = self.id + 1 if id is None else User._id_counter
        self.date_added = date_added if date_added is not None else datetime.datetime.now()

    def __str__(self):
        return (f"ID: {self.id}, ФИО: {self.full_name}, Телефон: {self.phone}, "
                f"Комментарий: {self.comment}, Дата добавления: {self.date_added}")


class Book:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.read_users()

    def read_users(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                User._id_counter = max([user['id'] for user in data], default=-1) + 1
                return [User(**user) for user in data]
        except FileNotFoundError:
            return []

    def save_book(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([user.__dict__ for user in self.users], file, ensure_ascii=False, default=str)

    def search_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.id != user_id]
        self.save_book()

    def edit_user(self, user_id, full_name=None, phone=None, comment=None):
        user = self.search_user(user_id)
        print(f'Вы отредактировали этого абонента {user}')
        if user:

            if full_name:
                user.full_name = full_name
            if phone:
                user.phone = phone
            if comment:
                user.comment = comment
            self.save_book()

    def add_user(self, full_name, phone, comment):
        new_user = User(full_name, phone, comment)
        self.users.append(new_user)
        print(f'user add {new_user}')  # Распечатать данные нового пользователя
        self.save_book()

    def reed_book(self):
        for user in self.read_users():
            print(user.id, user.full_name, user.phone, user.comment, user.date_added)

    def about_book(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                record_count = len(data)
                file_size = os.path.getsize(self.file_path)
                print(f"Количество записей телефонной книге: {record_count}")
                print(f"Размер файла: {file_size} байт")
        except FileNotFoundError:
            return []

class Menu:
    def __init__(self, book):
        self.book = book
        self.menu = {
            "0": ("Выйти из программы", lambda: False),
            "1": ("Информация о базе", lambda: (self.book.about_book(), True)),
            "2": ("Прочитать базу", lambda: (self.book.reed_book(), True)),
            "3": ("Добавить абонента", lambda: (self.book.add_user(
                input("Введите ФИО: "),
                input("Введите телефон: "),
                input("Введите комментарий: ")), True)),
            "4": ("Найти абонента", lambda: (print(self.book.search_user(int(input("Введите ID абонента: ")))), True)),
            "5": ("Удалить абонента", lambda: (self.book.remove_user(int(input("Введите ID абонента: "))), True)),
            "6": ("Изменить запись", lambda: (self.book.edit_user(
                int(input("Введите ID абонента: ")),
                input("Введите новое ФИО (оставьте пустым, если не нужно изменять): "),
                input("Введите новый телефон (оставьте пустым, если не нужно изменять): "),
                input("Введите новый комментарий (оставьте пустым, если не нужно изменять): ")), True))
        }

    def run(self):
        while True:
            print("\nМеню:")
            for key, value in self.menu.items():
                print(f"{key}. {value[0]}")

            choice = input("Выберите пункт меню: ")
            if choice in self.menu:
                result = self.menu[choice][1]()
                if result is False:
                    break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

