''' Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.'''


import os
from gen_name import generate_scenic_names
from rnd_num import generate_number_file

def multiply_and_save(names_file, numbers_file, output_file):
    # Генерируем имена в указанной директории
    directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar7_files"
    generate_scenic_names(8, directory, names_file)
    generate_number_file(10, directory, numbers_file)

    # Читаем имена из файла
    with open(os.path.join(directory, names_file), 'r') as names_file:
        names = [name.strip() for name in names_file.readlines()]

    # Читаем числа из файла
    with open(os.path.join(directory, numbers_file), 'r') as numbers_file:
        numbers = [tuple(map(float, line.strip().split('|'))) for line in numbers_file.readlines()]

    # Перемножаем числа и сохраняем результат в выходной файл
    with open(os.path.join(directory, output_file), 'w') as output_file:
        for name, (int_num, float_num) in zip(names, numbers):
            product = int_num * float_num
            if product < 0:
                product = abs(product)
                name = name.lower()
            else:
                product = round(product)
                name = name.upper()
            output_file.write(f"{name}: {product}\n")

if __name__ == '__main__':
    multiply_and_save('pseudonymous.txt', 'int-float.txt', 'number_name_multiplication.txt')
