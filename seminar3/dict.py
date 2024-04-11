a = {'one':32, 'two':31, 'ten':'Come to daddy'}
b = dict(one=32, two=31, ten='Come to daddy')
c = dict([('one',32), ('two',31), ('ten','Come to daddy')])
print(a==b==c)
my_dict = {'one':32, 'two':31, 'ten':'Come to daddy'}
print(my_dict.get('ten'))

'''
setdefault() возвращает значение и добавляет ключ в словарь
keys()    возвращает объект - итератор dict_keys
values()  возвращает объект - итератор dict_values
items() возвращает объект - итератор dict_items
popitem() удаляет последнюю пару ключ-значение
pop() удаляет пару ключ-значение по ключу
update() расширяет исходный словарь новыми парами
'''
my_dictionary = {'one': 1, 
                'two': 2,
                'three': 3,
                'four': 4,
                'ten': 10,}
print(my_dictionary.setdefault('ten', 555))
print(my_dictionary.values())
print(my_dictionary.pop('one'))

my_dictionary['one'] = my_dictionary['four']
print(my_dictionary)
