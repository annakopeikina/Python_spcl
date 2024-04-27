'''Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

import csv
import json
import os

def save_to_csv(json_file='users.json', csv_file='db.csv', directory='C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar8'):
    # Формируем путь к JSON файлу
    json_file_path = os.path.join(directory, json_file)

    # Проверяем существует ли файл JSON
    if not os.path.exists(json_file_path):
        print(f"Файл {json_file} не найден в директории {directory}.")
        return

    # Загружаем данные из JSON файла
    with open(json_file_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Формируем путь к CSV файлу
    csv_file_path = os.path.join(directory, csv_file)

    # Открываем CSV файл для записи
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        # Создаем объект writer
        writer = csv.writer(f)

        # Записываем заголовки
        writer.writerow(['Уровень доступа', 'Идентификатор', 'Имя'])

        # Записываем данные в CSV файл
        for access_level, users in db.items():
            for user_id, user_name in users.items():
                writer.writerow([access_level, user_id, user_name])

if __name__ == '__main__':
    save_to_csv()


'''
import json

def json_to_csv(name='users.json', res_file='db.csv'):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    
    with open(res_file, 'w', encoding='utf-8') as f:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f"{k},{k2},{v2}", file=f)

if __name__ == '__main__':
    json_to_csv()

'''