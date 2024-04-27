import pickle
import csv

def pickle_to_csv(pickle_file_path: str, csv_file_path: str) -> None:
    # Загрузить данные из pickle файла
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)

    # Если список словарей пуст, выйти из функции
    if not data:
        print("Ошибка: Пустой список словарей.")
        return

    # Получить ключи словаря для заголовков столбцов CSV
    keys = data[0].keys()

    # Записать данные в CSV файл
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)

        # Записать заголовки столбцов
        writer.writeheader()

        # Записать данные в CSV файл
        for item in data:
            writer.writerow(item)

# Пример использования функции
if __name__ == "__main__":
    pickle_file_path = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files/users_hashed_dict.pickle"
    csv_file_path = "C:/Users/akopeikina/OneDrive/Desktop/Python_spcl/hometask8_files/users_hashed_dict.csv"
    pickle_to_csv(pickle_file_path, csv_file_path)
