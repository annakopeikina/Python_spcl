"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
import random
import os

MAX_LEN = 7
MIN_LEN = 4
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"  # Согласные буквы

def generate_scenic_names(num_names, directory, filename):
    if num_names <= 0:
        print("Количество имен должно быть больше нуля.")
        return
    
    # Создаем полный путь к файлу
    filepath = os.path.join(directory, filename)

    # Проверяем существование файла
    if os.path.exists(filepath):
        # Генерируем новое имя файла, если файл уже существует
        i = 1
        while os.path.exists(filepath):
            filename, extension = os.path.splitext(filename)
            filename = f"{filename}_{i}{extension}"
            filepath = os.path.join(directory, filename)
            i += 1

    with open(filepath, 'w') as file:
        for _ in range(num_names):
            name_length = random.randint(MIN_LEN, MAX_LEN)
            name = ""
            prev_char_vowel = False  # флаг, указывающий, была ли предыдущая буква гласной
            for _ in range(name_length):
                if len(name) >= 2 and len(name) <= 4 and not prev_char_vowel:
                    # если длина имени от 2 до 4 и предыдущая буква не гласная, то добавляем гласную
                    char = random.choice(VOWELS)
                    prev_char_vowel = True
                elif prev_char_vowel:
                    # если предыдущая буква была гласной, то выбираем согласную
                    char = random.choice(CONSONANTS)
                    prev_char_vowel = False
                else:
                    # иначе выбираем случайную букву
                    char = random.choice(VOWELS + CONSONANTS)
                    prev_char_vowel = char in VOWELS
                name += char.lower()  # преобразуем букву к нижнему регистру и добавляем в имя
            file.write(name.capitalize() + '\n')

if __name__ == '__main__':
    directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar7_files"
    generate_scenic_names(8, directory, "scenic_names.txt")
