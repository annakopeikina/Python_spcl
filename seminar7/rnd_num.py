#Напишите функцию, которая заполняет файл
#(добавляет в конец) случайными парами чисел.
#Первое число int, второе - float разделены вертикальной чертой.
#Минимальное число - -1000, максимальное - +1000.
#Количество строк и имя файла передаются как аргументы функции.

import os
import random as rd

MIN_NUMBER = -1000
MAX_NUMBER = 1000

def generate_number_file(count: int, directory: str, filename: str = "random_numbers.txt"):
    '''Заполняет файл случайными числами'''

    # Создаем полный путь к файлу
    filepath = os.path.join(directory, filename)

    # Проверяем существование файла
    if os.path.exists(filepath):
        # Генерируем новое имя файла, если файл уже существует
        for i in range(1, 100):  # Ограничиваем количество попыток генерации нового имени
            new_filename, extension = os.path.splitext(filename)
            new_filename = f"{new_filename}_{i}{extension}"
            new_filepath = os.path.join(directory, new_filename)
            if not os.path.exists(new_filepath):
                filepath = new_filepath
                break
        else:
            raise FileExistsError("Не удалось сгенерировать уникальное имя файла")

    # Создаем файл и записываем в него случайные числа
    with open(filepath, 'w', encoding='utf-8') as file:
        for i in range(count):
            int_num = rd.randint(MIN_NUMBER, MAX_NUMBER)
            float_num = rd.uniform(MIN_NUMBER, MAX_NUMBER)
            file.write(f"{int_num}|{float_num}\n")

    return filepath

if __name__ == "__main__":
    directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar7_files"
    generate_number_file(10, directory)
