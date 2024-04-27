import csv
import json
import os

def save_to_csv(json_file='users.json', csv_file='db.csv', directory='C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files'):
    # Формируем путь к JSON файлу
    json_file_path = os.path.join(directory, json_file)

    # Проверяем существует ли файл JSON
    if not os.path.exists(json_file_path):
        print(f"Файл {json_file} не найден в директории {directory}.")
        return

    # Загружаем данные из JSON файла
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Получаем список пользователей
    users = data.get('users', [])

    # Формируем путь к CSV файлу
    csv_file_path = os.path.join(directory, csv_file)

    # Открываем CSV файл для записи
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        # Создаем объект writer
        writer = csv.DictWriter(f, fieldnames=['name', 'user_id', 'access_level'])

        # Записываем заголовки
        writer.writeheader()

        # Записываем данные в CSV файл
        writer.writerows(users)

if __name__ == '__main__':
    save_to_csv()
