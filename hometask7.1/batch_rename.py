import os

def batch_rename_files(directory, desired_name, digit_count, original_extension, new_extension, name_range=None):
    """
    Пакетно переименовывает файлы в указанном каталоге в соответствии с заданными параметрами.

    Аргументы:
    directory (str): Каталог, содержащий файлы, которые нужно переименовать.
    desired_name (str): Желаемое конечное имя для файлов.
    digit_count (int): Количество цифр в числовом суффиксе.
    original_extension (str): Исходное расширение файлов, которые нужно переименовать.
    new_extension (str): Желаемое новое расширение для файлов.
    name_range (tuple): Диапазон символов, которые нужно оставить из исходного имени файла (включительно).
                        Формат: (начальный_индекс, конечный_индекс). По умолчанию None (без диапазона).

    Возвращает:
    None
    """
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print("Каталог не найден.")
        return

    files_to_rename = [f for f in os.listdir(directory) if f.endswith(original_extension)]
    if not files_to_rename:
        print("Файлы с указанным расширением не найдены.")
        return

    counter = 1
    for filename in files_to_rename:
        name, extension = os.path.splitext(filename)
        new_name = ""
        if name_range is not None:
            start_index, end_index = name_range
            new_name += name[start_index - 1:end_index]
        new_name += desired_name
        new_name += f"{counter:0{digit_count}d}.{new_extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        counter += 1

if __name__ == "__main__":
    # Пример использования функции
    directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask7_files"
    desired_name = "file"
    digit_count = 3
    original_extension = ".txt"
    new_extension = "dat"
    name_range = (1, 3)  #  буквы в имени файла
    batch_rename_files(directory, desired_name, digit_count, original_extension, new_extension, name_range)
