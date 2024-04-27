#hometask8.1 == my_package8.1 ( в случаях использования в проектах)

#1 конвертирует существующий файл в формат JSON
''' from .text_to_json import text_to_json'''

#2 создаёт список пользователей с id номером в формате JSON
''' from .users_manager_json import add_user_to_json '''

#3 сохраняет созданный файл в формате CSV
''' from json_to_csv import save_to_csv'''

#4 читатает CSV файл без использования csv.DictReader.
    # дополняет идентификаторы до 10 цифр незначащими нулями
    # делает первую букву имени прописной
    # добавляет поле хеш на основе имени и идентификатора
    # cохраняет полученные записи в JSON файл, где каждая строка CSV файла будет представлена как отдельный JSON словарь
''' from csv_to_json_dicts import process_csv_to_json'''

#5 ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов
'''from pick_json_to_pickle import json_to_pickle '''

#6 преобразует pickle файл хранящий список словарей в табличный csv файл, извлекает ключи словаря
    # для заголовков столбца из переданного файла
''' from pickle_to_csv_table import pickle_to_csv '''

#7 читает созданный csv файл без использования csv.DictReader, распечатывает  его как pickle строку
''' from csv_to_pickle import csv_to_pickle'''

