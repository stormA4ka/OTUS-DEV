from model import Book
from view import View
from controller import Controller

if __name__ == '__main__':

    file_path = 'users.json' # путь к базе
    book = Book(file_path) # Создаем экземпляр класса Book
    view = View()
    controller = Controller(book, view)
    controller.run()


    print('job done')