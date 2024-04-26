# CSV(comma-Separated Values)

import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))

csv_write = csv.write = csv.writer(f) # позволяет сохранять данные  в формате CSV

csv_write.writerow(line) # сохранение списка в одной строке файла в формате CSV

csv_write.writerows('''all_data''') #сохранение матрицы (список списков) в нескольких строках файла в формате CSV

