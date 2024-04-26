import csv

with (
    open("'''biostats_tab.csv'''", 'r', newline='') as f_read,
    open("'''biostats.csv'''", 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel' , delimiter=' ' , quatechar='|' , quoting=csv.QUOTE_MINIMAL)
    all_data = []

    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2,4 +1):
                line[j] = int(line[j])
            all_data.append(line)
        csv_write.writerows(all_data)

csv_file = csv.DictReader(f, fieldnames=["name","sex","age","height", "weight","office"], restkey="new", restval="Main Office")

# fieldnames-список заголовков столбцов, ключей словаря
# restkey - значение ключа для столбцов, которых нет в fieldnames
# restval - значение поля для ключей fieldnames, которых нет в файле CSV

import csv

# Открываем CSV файл для чтения
with open("biostats_tab.csv", 'r', newline='') as f:
    # Создаем объект DictReader для чтения CSV файла как словаря
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restkey="new", restval="Main Office", dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)

    # Читаем и печатаем каждую строку из CSV файла
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"]= }\t{line["age"]=}')

# Открываем файл для записи
with open("output.csv", 'w', newline='') as f_write:
    # Создаем объект writer для записи данных в CSV файл
    csv_writer = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


# csv_write.writeheader - из [age],[name],[wheight] - сделать заголовки столбцов