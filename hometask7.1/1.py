import os
from batch_rename import batch_rename_files


if __name__ == "__main__":
    # Пример использования функции
    directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask7_files"
    desired_name = "file"
    digit_count = 3
    original_extension = ".txt"
    new_extension = "dat"
    name_range = (3, 6)  # От третьей до шестой буквы в имени файла
    batch_rename_files(directory, desired_name, digit_count, original_extension, new_extension, name_range)
