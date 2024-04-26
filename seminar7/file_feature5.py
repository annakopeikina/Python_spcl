import os

file_path = r"C:\Users\akopeikina\OneDrive\Desktop\Python_spcl\seminar7\mate.txt"


last = before = 0
text = ["метод изменяет размер файла. Если не передать значение в параметр size будет удалена часть файла от текущей позиции"]

with open(file_path, 'r+', encoding='utf-8') as f:
    while line :=f.readline(): 

        """Это выражение использует новую возможность Python 3.8+ под названием "оператор присваивания
        с условием" (walrus operator). Это новый способ присваивания переменной значения в Python.
        line :=: Это оператор присваивания с условием. Он присваивает результат f.readline() переменной line
        и одновременно проверяет, что line не равно пустой строке или None. Если line не пустая строка (или не None),
        то выражение line := f.readline() вернет True и выполнение цикла продолжится."""

        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before,0) = }')
    f.write('\n'.join(text))
