# users_manager_json.py

import json
import os

def add_user_to_json():
    # Путь к папке для сохранения файлов
    output_directory = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files"
    # Создаем папку, если она не существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Путь к файлу JSON в папке hometask8_files
    json_file_path = os.path.join(output_directory, 'users.json')
    print("Путь к файлу JSON:", json_file_path)  # Добавим отладочный вывод

    # Проверяем, существует ли JSON файл, если нет, создаем его
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as f:
            json.dump({'users': []}, f)

    # Загружаем данные из JSON файла
    with open(json_file_path, 'r') as f:
        users_data = json.load(f)

    users = users_data['users']

    while True:
        name = input("Введите имя пользователя: ")
        user_id = input("Введите личный идентификатор пользователя: ")

        # Проверяем уникальность идентификатора пользователя
        if any(user['user_id'] == user_id for user in users):
            print("Этот идентификатор уже используется, введите другой.")
            continue

        access_level = int(input("Введите уровень доступа пользователя (от 1 до 7): "))
        user = {"name": name, "user_id": user_id, "access_level": access_level}
        users.append(user)

        # Записываем обновленные данные в JSON файл
        with open(json_file_path, 'w') as f:
            json.dump(users_data, f, indent=4)

        choice = input("Хотите добавить еще одного пользователя? (да/нет): ")
        if choice.lower() != 'да':
            break

# Пример вызова функции
if __name__ == '__main__':
    add_user_to_json()
