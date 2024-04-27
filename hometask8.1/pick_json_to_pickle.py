import json
import pickle
from pathlib import Path

def json_to_pickle(directory: str) -> None:
    # Проверяем, что директория существует
    if not Path(directory).is_dir():
        print(f"Директория {directory} не существует.")
        return
    
    # Ищем JSON файлы в указанной директории
    json_files = list(Path(directory).glob("*.json"))

    # Обработка каждого найденного JSON файла
    for json_file in json_files:
        # Формируем имя для pickle файла
        pickle_file = json_file.with_suffix('.pickle')

        # Загружаем JSON файл
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Сохраняем данные в файл pickle
        with open(pickle_file, 'wb') as pkl_file:
            pickle.dump(data, pkl_file)
            print(f"Файл {json_file} успешно сохранен как {pickle_file}.")

if __name__ == '__main__':
    # Укажите путь к директории, в которой нужно искать JSON файлы
    directory_path = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files"

    # Вызываем функцию для обработки файлов в указанной директории
    json_to_pickle(directory_path)