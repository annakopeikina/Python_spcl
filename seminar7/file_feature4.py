# записывает сразу в файл, не выводит на консоль

import os

file_path = r"C:\Users\akopeikina\OneDrive\Desktop\Python_spcl\seminar7\mate.txt"


text = ['Создаем новый пустой файл для записи если файл существует открываем его для записей удаляем данные которые в нем хранились\\']

with open(file_path, 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file = f)
        

# Методы перемещения в файле

''' f.tell() -метод tell возвращает текущую позицию в файле 
    seek(offset, whence=0)  - offset -смещение относительно опорной точки , whence - способ выбора опорной точки:
            whence=0 -отсчет от начала файла
            whence=1 - отсчет от текущего положения файла
            whence=2 - отсчет от конца файла
    trancate(size=None) -метод изменяет размер файла. Если не передать значение в параметр size будет удалена часть
                        файла от текущей позиции

                        '''
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell()) 
print(f.tell())