#_________срезы______list[start:stop:step]

import copy


my_list = [6,5,4,6,77,55,5,6,5,7,8,99,536]
print(my_list[2:10:2])
print(my_list[:10:2]) # если пропущен индекс -старт по умолчанию 0
print(my_list[2::2]) # по умолчанию до конца
print(my_list[2:7:]) # по умолчанию step=1
print(my_list[8:3:-1]) # справа налево
print(my_list[3::])
print(my_list[:7:])

#_________метод copy()_________создаёт поверхностную копиюmy
my_list = [2,5,4,6,43,5,34,567,5,86]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
new_list[2] = 555
print(my_list, new_list, sep='\n')




#_______функция copy.deepcopy()_____рекурсивно создаёт полную копию
matrix = [[1,2,3],[2,3,4],[4,5,6]]
new_m = matrix.copy()
print(matrix, new_m,sep='\n')
matrix[0][1] = 555
print(matrix, new_m,sep='\n')

matrix = [[1,2,3],[2,3,4],[4,5,6]]
new_m =copy.deepcopy(matrix)
print(matrix, new_m,sep='\n')
matrix[0][1] = 555
print(matrix, new_m,sep='\n')