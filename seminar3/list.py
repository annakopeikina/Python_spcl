list_1 = list()
list_2 = list((3.14, True, "Carma Comma"))#динамический массив ссылающийся на все объекты
list_3 = []# список 3=2


my_list = [2,4,6,8,10,12]
print(my_list[0])#берет индекс__ 2
#print(my_list[-10]) # IndexError:list index out of range
print(my_list[-1]) # может быть отрицательная индексация, обращаются к элементу с конца,
                    # не слева направо, а справа налево=>__ 12

# ___________________append добавляет к сушествующему списку новые значения__________

a =40
b='karma comma'
c=[1,3,5,7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b) #ссылки на объекты с неограничной вложенностью
print(my_list)
my_list.append(c)
print(my_list)

#зацикливание: добавить my_list в my_list
#my_list.append(my_list)
#print(my_list)

#____________extend рассширяет список____________________________________

a=40
b='karmacomma'
c=[1,3,5,7]
my_list=[None]
#my_list.extend(a)
print(my_list)
my_list.extend(b) #[None, 40, 'karma comma', [1, 3, 5, 7]]
#[None]
#[None, 'k', 'a', 'r', 'm', 'a', 'c', 'o', 'm', 'm', 'a']
#[None, 'k', 'a', 'r', 'm', 'a', 'c', 'o', 'm', 'm', 'a', 1, 3, 5, 7]
#[None, 'k', 'a', 'r', 'm', 'a', 'c', 'o', 'm', 'm', 'a', 1, 3, 5, 7]




print(my_list)
my_list.extend(c)
print(my_list)
#my_list.extend(my_list)
print(my_list)

#________________pop__________удаляет элементы из списка без добавления значений
# по индексу 
my_list = [2,3,4,7,8,12,22,2222]
spam = my_list.pop()
print(spam, my_list)
eggs =my_list.pop()
print(eggs, my_list)
#err = my_list.pop(13) #IndexError: pop index out of range

#__________________count________________
#__________________index________________поиск первого вхождения элемента в список
my_list=[2,4,6,8,10,12,2,4,14,2]
wow = my_list.index(4)
print(wow)
spring = my_list.index(4, wow + 1, 90)
print(spring)

#_____________insert_________________увеличение исходного списка на 1 элемент, 
#следующие по индексу сдвигаются на одну ячейку в сторону
my_list.insert(12,41) # первый аргумент - индекс, второй-значение тождество:.append()
# добавляет в конец списка, а insert может добавить и в середину по индексу
print(my_list)

#____________remove________удаляет элемент не по индексу а по значению
my_list=[2,4,6,8,10,12,2,4,14,2]
my_list.remove(2)

print(my_list)

# ____функция sorted() и метод sort()______


#_______функуия reversed() и метод reverse()________


#Syntaxis [::-1]

#как можно изменить порядок элементов внутри списков

#sorted
my_list = [3,4,2,56,7,4]
sort_list = sorted(my_list)
print(my_list,sort_list, sep='\t')
rev_list = sorted(my_list, reverse = True)
print(my_list, rev_list, sep='\t')
