'''Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.'''

import os

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    'png': 'pictures',
}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = os.path.join(directory, DICTIONARY[extension])
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.makedirs(new_directory)
        os.rename(os.path.join(directory, f), os.path.join(new_directory, f))

if __name__ == '__main__':
    # Путь к папке "Downloads"
    downloads_directory = "C:/Users/akopeikina/Downloads"
    sort_files(downloads_directory)


    
'''import os
import shutil

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    'png': 'pictures',
}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = os.path.join(directory, DICTIONARY[extension])
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.makedirs(new_directory)
        shutil.move(os.path.join(directory, f), os.path.join(new_directory, f))

if __name__ == '__main__':
    # Путь к папке "Downloads"
    downloads_directory = "C:/Users/akopeikina/Downloads"
    sort_files(downloads_directory)

'''