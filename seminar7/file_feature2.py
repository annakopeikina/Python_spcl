import os

file_path = r"C:\Users\akopeikina\OneDrive\Desktop\Python_spcl\seminar7\mate.txt"

if os.path.isfile(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print(list(f))
else:
    print("Файл не найден.")

              # Менеджер контекста with Open                        #  with - Гарантирует закрытие файла сохранения информации

with open(file_path, 'a', encoding='utf-8') as f:
    f.write('  как адамово яблоко\n')

''' 

    buffering -определяет режим буферизации
    errors -используют только в текстовом режиме и определяет поведение в случае ошибок кодирования или декодирования
    newline -отвечает за преобразование окончания строки
    closefd -указывает оставлятьли файловый дескриптор открытым при закрытии файла\
    opener - позволяет передать пользовательскую функцию для открытия файла


with open('text.txt', 'r', encoding='utf-8') as f1, \
        open('bin_data', 'rb') as f2, \
        open('data_txt.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))  '''
# Чтение файла
'''
list(f) -чтение в список
res = f.read() - чтение методом read 
res = f.readline() - чтение методом readline
for line in f: - чтение циклом for



'''
SIZE = 100
with open(file_path, 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)

SIZE = 10
with open(file_path, 'r', encoding='utf-8') as f:
    res = f.readline(SIZE)
    print(res)

SIZE = 3
with open(file_path, 'r', encoding='utf-8')as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))


