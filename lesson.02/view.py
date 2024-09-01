class View:
    @staticmethod
    def display_menu(menu):
        print("\nМеню:")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")

    @staticmethod
    def display_user(user):
        print(user)

    @staticmethod
    def display_book(users):
        for user in users:
            print(user.id, user.full_name, user.phone, user.comment, user.date_added)

    @staticmethod
    def display_about_book(record_count, file_size):
        print(f"Количество записей телефонной книге: {record_count}")
        print(f"Размер файла: {file_size} байт")

    @staticmethod
    def get_input(prompt):
        return input(prompt)