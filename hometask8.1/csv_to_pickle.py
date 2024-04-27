import csv
import pickle

def csv_to_pickle(csv_file):
    # Читаем первую строку для создания заголовков
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        header_row = next(csv.reader(f))
    
    # Создаем заголовки для данных
    headers = [f'field_{i}' for i in range(len(header_row))]

    # Читаем данные, преобразуя их в словари с использованием csv.DictReader
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f, fieldnames=headers)
        data = [row for row in csv_reader]

    # Преобразуем данные в строку pickle
    pickle_string = pickle.dumps(data)
    return pickle_string

if __name__ == "__main__":
    csv_file = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files/db.csv"
    pickle_string = csv_to_pickle(csv_file)
    print(pickle_string)

    # Пример загрузки pickle строки обратно в данные
    loaded_data = pickle.loads(pickle_string)
    print(loaded_data)
