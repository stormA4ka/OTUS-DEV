import os
import msvcrt
import sys
from openpyxl import load_workbook, Workbook
from datetime import datetime
import pandas as pd



def search_rows(dir_path, file_name):
    """
    Выбор колонки для поиска и поиск строк по введенным значениям.

    :param df: DataFrame для поиска
    :return: Список ID найденных строк
    """

    file_path = os.path.join(dir_path, file_name)
    df = pd.read_excel(file_path)
    cols = ["ID", "ФИО", "Телефон", "Комментарий", "Дата добавления"]
    print("Доступные колонки для поиска:")
    for i, col in enumerate(cols):
        print(f"{i + 1}. {col}")

    # Запрашиваем выбор колонки
    col_choice = int(input("Выберите номер колонки для поиска: ")) - 1
    selected_col = cols[col_choice]

    # Запрашиваем ввод значений для выбранной колонки
    values_input = input(f"Введите значения для поиска в колонке '{selected_col}' (через запятую, если несколько): ")
    values = [value.strip() for value in values_input.split(",") if value.strip()]

    # Преобразуем значения в соответствии с типом данных в колонке
    if selected_col == "ID":
        try:
            values = [int(value) for value in values]
        except ValueError:
            print("Ошибка: значения в колонке 'ID' должны быть числами.")
            return []

    # Создаем условие для фильтрации
    condition = df[selected_col].isin(values)

    # Находим строки, соответствующие условию
    rows_to_remove = df[condition]

    # Возвращаем список ID найденных строк
    return rows_to_remove, rows_to_remove['ID'].tolist()



def edit_row(dir_path, file_name):
    """
    Находит и редактирует строку в DataFrame на основе значения в указанной колонке.
    После редактирования сохраняет изменения в файл Excel.

    :param dir_path: Путь к директории с файлом
    :param file_name: Имя файла
    :return: DataFrame с отредактированной строкой
    """
    file_path = os.path.join(dir_path, file_name)
    df = pd.read_excel(file_path)

    # Вызываем функцию поиска строки для редактирования
    rows_to_edit, ids_to_edit = search_rows(dir_path, file_name)

    # Проверяем, есть ли строки для редактирования
    if not rows_to_edit.empty:
        print("Найдены следующие записи:")
        print(rows_to_edit)
        confirm = input("Точно редактировать эти записи? (y/n): ")
        if confirm.lower() == 'y':
            # Запрашиваем новые значения для каждой колонки
            editable_cols = ["ФИО", "Телефон", "Комментарий"]
            new_values = {}
            for col in editable_cols:
                new_value = input(f"Введите новое значение для колонки '{col}' (оставьте пустым, чтобы не изменять): ")
                if new_value:
                    new_values[col] = new_value

            # Обновляем строки в DataFrame
            for index in rows_to_edit.index:
                for col, new_value in new_values.items():
                    df.at[index, col] = new_value

            print("Записи отредактированы.")
            df.to_excel(file_path, sheet_name='Sheet', index=False)
            return df
        else:
            print("Записи не отредактированы.")
            return df
    else:
        print("Записи не найдены.")
        return df

# Пример использования функции
if __name__ == "__main__":
    PATH = '../proj_telbook/db'
    FILE = 'tel_book.xlsx'
    edit_row(PATH, FILE)

# Пример использования функции
if __name__ == "__main__":
    PATH = '../proj_telbook/db'
    FILE = 'tel_book.xlsx'
    edit_row(PATH, FILE)