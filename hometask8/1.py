# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_directory_info(directory):
    # Функция для получения информации о директории и всех ее поддиректориях

    # Структура данных для хранения информации о файлах и поддиректориях
    directory_info = {
        'name': os.path.basename(directory),
        'type': 'directory',
        'size': 0,  # Размер директории в байтах (изначально ноль)
        'contents': []  # Список для хранения информации о содержимом директории
    }

    # Обход содержимого директории
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Если это файл, получаем его информацию
            file_info = {
                'name': item,
                'type': 'file',
                'size': os.path.getsize(item_path)  # Размер файла в байтах
            }
            directory_info['contents'].append(file_info)
            directory_info['size'] += file_info['size']  # Увеличиваем размер директории
        elif os.path.isdir(item_path):
            # Если это директория, рекурсивно получаем ее информацию
            subdirectory_info = get_directory_info(item_path)
            directory_info['contents'].append(subdirectory_info)
            directory_info['size'] += subdirectory_info['size']  # Увеличиваем размер директории

    return directory_info

def save_to_json(data, filename):
    # Функция для сохранения данных в формате JSON
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    # Функция для сохранения данных в формате CSV
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Type', 'Size'])  # Заголовки
        write_csv_row(writer, data)

def write_csv_row(writer, data):
    # Вспомогательная функция для записи строки в CSV файл
    if data['type'] == 'directory':
        for item in data['contents']:
            write_csv_row(writer, item)
    else:
        writer.writerow([data['name'], data['type'], data['size']])

def save_to_pickle(data, filename):
    # Функция для сохранения данных в формате Pickle
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

if __name__ == '__main__':
    # Укажите путь к директории, которую нужно обойти
    directory_to_traverse = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar8"

    # Укажите путь к директории, в которой нужно сохранить результаты
    output_directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8"

    # Получаем информацию о директории
    directory_info = get_directory_info(directory_to_traverse)

    # Сохраняем данные в файлы различных форматов
    save_to_json(directory_info, os.path.join(output_directory, 'directory_info.json'))
    save_to_csv(directory_info, os.path.join(output_directory, 'directory_info.csv'))
    save_to_pickle(directory_info, os.path.join(output_directory, 'directory_info.pickle'))

