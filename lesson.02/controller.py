from model import Book
from view import View

class Controller:
    def __init__(self, book, view):
        self.book = book
        self.view = view
        self.menu = {
            "0": ("Выйти из программы", self.exit_program),
            "1": ("Информация о базе", self.about_book),
            "2": ("Прочитать базу", self.reed_book),
            "3": ("Добавить абонента", self.add_user),
            "4": ("Найти абонента", self.search_user),
            "5": ("Удалить абонента", self.remove_user),
            "6": ("Изменить запись", self.edit_user)
        }

    def run(self):
        while True:
            self.view.display_menu(self.menu)
            choice = self.view.get_input("Выберите пункт меню: ")
            if choice in self.menu:
                result = self.menu[choice][1]()
                if result is False:
                    break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def exit_program(self):
        return False

    def about_book(self):
        record_count, file_size = self.book.about_book()
        self.view.display_about_book(record_count, file_size)
        return True

    def reed_book(self):
        users = self.book.reed_book()
        self.view.display_book(users)
        return True

    def add_user(self):
        full_name = self.view.get_input("Введите ФИО: ")
        phone = self.view.get_input("Введите телефон: ")
        comment = self.view.get_input("Введите комментарий: ")
        new_user = self.book.add_user(full_name, phone, comment)
        self.view.display_user(new_user)
        return True

    def search_user(self):
        user_id = int(self.view.get_input("Введите ID абонента: "))
        user = self.book.search_user(user_id)
        self.view.display_user(user)
        return True

    def remove_user(self):
        user_id = int(self.view.get_input("Введите ID абонента: "))
        self.book.remove_user(user_id)
        return True

    def edit_user(self):
        user_id = int(self.view.get_input("Введите ID абонента: "))
        full_name = self.view.get_input("Введите новое ФИО (оставьте пустым, если не нужно изменять): ")
        phone = self.view.get_input("Введите новый телефон (оставьте пустым, если не нужно изменять): ")
        comment = self.view.get_input("Введите новый комментарий (оставьте пустым, если не нужно изменять): ")
        self.book.edit_user(user_id, full_name, phone, comment)
        return True