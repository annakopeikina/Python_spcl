'''Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''
'''
import csv
import json

def csv_to_json(input_csv_file, output_json_file):
    # Создаем список для хранения данных из CSV файла
    data = []
    
    # Открываем CSV файл для чтения
    with open(input_csv_file, 'r', newline='') as f:
        # Создаем объект DictReader для чтения CSV файла как словаря
        csv_file = csv.DictReader(f)
        
        # Читаем каждую строку из CSV файла и добавляем ее в список данных
        for line in csv_file:
            data.append({key.capitalize(): value for key, value in line.items()})
    
    # Открываем JSON файл для записи
    with open(output_json_file, 'w') as f:
        # Записываем данные в JSON файл
        json.dump(data, f, indent=4)

# Путь к CSV файлу, который нужно конвертировать
input_csv_file = "biostats_tab.csv"

# Путь к JSON файлу, в который нужно записать данные
output_json_file = "output.json"

# Вызываем функцию для конвертации CSV в JSON
csv_to_json(input_csv_file, output_json_file)
'''


import json


def text_to_json(name='res.txt'):
    with open(name, 'r', encoding='utf-8') as f, \
         open('res.json', 'w', encoding='utf-8') as f2:
        res_list = []
        for line in f:
            res_list.append(line.strip().capitalize())
        json.dump(res_list, f2, indent=4)

if __name__ == '__main__':
    text_to_json()
