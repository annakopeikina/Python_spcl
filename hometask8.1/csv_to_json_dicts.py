import json
from pathlib import Path

def process_csv_to_json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        # Прочитать CSV файл
        for line in f:
            # Разделить строку CSV на поля
            level, user_id, name = line.strip().split(',')
            
            # Дополнить идентификатор нулями до 10 цифр
            padded_id = user_id.zfill(10)
            
            # Сделать первую букву имени прописной
            capitalized_name = name.capitalize()
            
            # Создать хеш на основе имени и идентификатора
            name_id_hash = hash(f"{capitalized_name}{padded_id}")
            
            # Создать JSON словарь для текущей записи
            json_dict = {
                'level': level,
                'id': padded_id,
                'name': capitalized_name,
                'hash': name_id_hash
            }
            
            # Добавить JSON словарь в список
            json_list.append(json_dict)
    
    # Сохранить записи в JSON файл с переименованием
    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)

# Пример использования функции
if __name__ == '__main__':
    from_file = Path('C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files/db.csv')
    to_file = Path('C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files/users_hashed_dict.json')
    process_csv_to_json(from_file, to_file)
