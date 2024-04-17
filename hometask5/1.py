# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def split_file_path(file_path: str) -> tuple:
    """
    Разбивает абсолютный путь до файла на путь, имя файла и расширение файла.

    Args:
        file_path (str): Абсолютный путь до файла.

    Returns:
        tuple: Кортеж из трех элементов: путь, имя файла, расширение файла.
    """
    file_dir, file_name = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(file_name)
    return file_dir, file_name, file_ext

file_path = "C:\\Users\\akopeikina\\OneDrive\\Documents\\my_sql_homework6.txt"
result = split_file_path(file_path)
print(result)
