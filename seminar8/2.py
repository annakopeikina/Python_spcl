'''Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''
import json
import os

def add_user_to_json():
    # Формируем путь к файлу JSON
    json_file_path = os.path.join(os.getcwd(), 'seminar8', 'users.json')

    # Проверяем, существует ли JSON файл, если нет, создаем его
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as f:
            json.dump({}, f)

    # Загружаем данные из JSON файла
    with open(json_file_path, 'r') as f:
        users = json.load(f)

    while True:
        name = input("Введите имя пользователя: ")
        user_id = input("Введите личный идентификатор пользователя: ")
        access_level = int(input("Введите уровень доступа пользователя (от 1 до 7): "))

        # Проверяем уникальность идентификатора пользователя
        if user_id in users.values():
            print("Этот идентификатор уже используется, введите другой.")
            continue

        # Добавляем информацию о пользователе в соответствующий уровень доступа
        if access_level not in users:
            users[access_level] = {}
        users[access_level][user_id] = {"name": name}

        # Записываем обновленные данные в JSON файл
        with open(json_file_path, 'w') as f:
            json.dump(users, f, indent=4)

        choice = input("Хотите добавить еще одного пользователя? (да/нет): ")
        if choice.lower() != 'да':
            break

if __name__ == '__main__':
    add_user_to_json()

''' import json
import os

def access_users(name='db.json'):
    db = {}

    # Проверяем существует ли файл и является ли он файлом
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)

    while True:
        try:
            user_level = int(input('Введите уровень доступа от 1 до 7 или любую букву для выхода: '))
        except ValueError:
            # Если введена буква, завершаем цикл
            with open(name, 'w', encoding='utf-8') as f:
                json.dump(db, f, indent=4)
            exit()
        else:
            if not 1 <= user_level <= 7:
                continue

        if user_level not in db:
            db[user_level] = {}

        while True:
            try:
                user_id = int(input('Введите идентификатор: '))
            except ValueError:
                print('Вы ввели не число!')
            else:
                if user_id in db.get(user_level, {}).keys():
                    print('Идентификатор должен быть уникальным!')
                    continue
                break

        while True:
            user_name = input('Введите имя: ')
            if user_name:
                break
            else:
                print('Имя не должно быть пустым!')

        db[user_level][user_id] = user_name

if __name__ == '__main__':
    access_users()

'''