"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 2
Имя файла и его размер должны быть в рамках переданного диапазона.
"""

import os
import random
import string

MIN_LETTER = ord('a')
MAX_LETTER = ord('z')

def generate_text(length):
    """Генерирует случайное имя файла."""
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
    return "".join(name)

def generate_files(extension, directory, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, num_files=2):
    """Генерирует файлы с заданными параметрами."""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.makedirs(directory)
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        filename = generate_text(name_length)
        # Проверяем, существует ли файл с таким же именем
        counter = 1
        while os.path.exists(os.path.join(directory, f"{filename}_{counter}.{extension}")):
            counter += 1
        text_length = random.randint(min_bytes, max_bytes)
        text = ''.join(random.choices(string.ascii_letters + string.digits, k=text_length))
        with open(os.path.join(directory, f"{filename}_{counter}.{extension}"), 'w', encoding='utf-8') as f:
            f.write(text)

if __name__ == '__main__':
    generate_files('txt', 'C:\\Users\\akopeikina\\OneDrive\\Desktop\\Python_spcl\\hometask7_files')
