'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
'''
import csv
import json
from pathlib import Path

def csv_to_json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader)  # Пропускаем заголовки
        
        for line in csv_reader:
            level, user_id, name = line
            
            # Дополнение идентификатора нулями до 10 цифр
            padded_id = user_id.zfill(10)
            
            # Прописываем первую букву имени
            capitalized_name = name.capitalize()
            
            # Генерируем хеш на основе имени и идентификатора
            name_id_hash = hash(f"{capitalized_name}{padded_id}")
            
            # Создаем словарь для JSON записи
            json_dict = {
                'level': int(level),
                'id': padded_id,
                'name': capitalized_name,
                'hash': name_id_hash
            }
            
            json_list.append(json_dict)
    
    # Сохраняем записи в JSON файл
    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)

if __name__ == '__main__':
    csv_to_json(Path('C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/seminar8/users.json'), Path('users.json'))

