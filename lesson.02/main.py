from model import Book
from view import View
from controller import Controller

if __name__ == '__main__':

    file_path = 'users.json' # путь к базе
    book = Book(file_path) # Создаем экземпляр класса Book


    # Добавление пользователя
    # book.add_user("Дейл", "+70000000099", "Ищет приключения")

    # # Поиск пользователя
    # user = book.search_user(1)
    # print(user)

    # # Редактирование пользователя
    # book.edit_user(0, comment="Измененный комментарий")

    # # Удаление пользователя
    # book.remove_user(2)

    # Читаем базу
    # for user in book.users:
    #     print(user)

    # Читаем базу 2
    # book.reed_book()

    # Информация о книге
    # book.about_book()





    view = View()
    controller = Controller(book, view)
    controller.run()


    print('job done')