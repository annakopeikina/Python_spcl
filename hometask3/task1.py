#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import random
def remove_duplicates(lst):
    return list(set(lst))
random_list = [random.randint(1, 10) for _ in range(10)]
print("Исходный случайный список:", random_list)

result = remove_duplicates(random_list)
print("Список без дубликатов:", result)
