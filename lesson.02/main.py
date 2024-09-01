from model import User, Book, Menu

if __name__ == '__main__':

    # путь к базе
    file_path = 'users.json'
    # Создаем экземпляр класса Book
    book = Book(file_path)


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




    menu = Menu(book)
    menu.run()


    print('job done')