import os

file_path = r"C:\Users\akopeikina\OneDrive\Desktop\Python_spcl\seminar7\mate.txt"

if os.path.isfile(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print(list(f))
else:
    print("Файл не найден.")

    #  Менеджер контекста with Open # with -  Гарантирует закрытие файла сохранения информации
