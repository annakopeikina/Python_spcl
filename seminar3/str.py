#__str
text='Karmacomma'
print(text[6])
print(text[3:8])
#Метод insert() изменяет список на месте и не возвращает ничего,
# поэтому присвоение my_list = new_text.insert(5, "-") приведет к тому,
# что my_list будет равно None.

'''
new_text = text.replace('m', 'l') # ещё один аргумент будет означать количество замен
my_list = new_text.insert(5, "-")
print(text, my_list, sep='\n')
'''
#
text = 'Karmacomma'

# Превращаем строку в список символов
my_list = list(text)

# Вставляем дефис после 5-го символа
my_list.insert(5, '-')

# Преобразуем список обратно в строку
new_text = ''.join(my_list)

# Заменяем символы 'm' на 'l'
new_text = new_text.replace('m', 'l')

print(text[6])      # Выводит символ 'o'
print(text[3:8])    # Выводит 'macom'

print(new_text)     # Выводит 'Karla-colla'

# _________________string format________
#format
name = 'Karla-colla'
age = 12
text = 'Меня зовут {} и мне {} лет выдержки'.format(name,age)
print(text)

#f-строка
name = 'Karla-colla'
age = 12
text = f'Rapasonic любит {name}  {age} летней выдержки и более того'
print(text)

print(f'{{Figured brackets}} и {{name}}')

pi_value = 3.1415  
print(f'число пи с точностью до третьего знака: {pi_value:.3f}')

data = [3234, 24245,9,34234345,34343252354,3434,2525]
for item in data:
    print(f'{item:^10}')

num = 2 * pi_value * data[1]
print(f'{num = :_}')

text = "Romb of Rumba is ROunDED by Rom"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())
print(text.capitalize())





