#1. Напишите функцию для транспонирования матрицы

import numpy as np

def transpose_matrix(matrix) -> list[list]:
    """
    Функция для транспонирования матрицы.

    Принимает матрицу в виде списка списков и возвращает транспонированную матрицу.
    """
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

if __name__ == '__main__':
    # Генерация случайной матрицы размером 3x3
    random_matrix = np.random.randint(1, 10, size=(3, 3)).tolist()  # Преобразуем массив NumPy в список списков
    print("Исходная матрица:")
    for column in random_matrix:
        print(column)

    # Транспонирование матрицы
    transposed = transpose_matrix(random_matrix)
    print("Транспонированная матрица:")
    for row in transposed:
        print(row)

