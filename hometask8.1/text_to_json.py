import json
import os

def text_to_json(name='name_number_multiplication.txt'):
    # Создаем папку для файлов, если её еще нет
    output_directory = 'hometask8_files'
    os.makedirs(output_directory, exist_ok=True)
    
    # Определяем имя и расширение исходного файла
    filename, _ = os.path.splitext(os.path.basename(name))
    # Формируем путь к JSON файлу в папке hometask8_files
    json_path = os.path.join(output_directory, f'{filename}.json')

    with open(name, 'r', encoding='utf-8') as f, \
         open(json_path, 'w', encoding='utf-8') as f2:
        name_number_multiplication_list = []
        for line in f:
           name_number_multiplication_list.append(line.strip().capitalize())
        json.dump(name_number_multiplication_list, f2, indent=4)

# Пример вызова функции
if __name__ == '__main__':
    text_to_json('C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar8/name_number_multiplication.txt')

