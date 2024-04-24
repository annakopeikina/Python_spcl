'''buffering - Определяет режим буферизации
errors - Используется только в текстовом режиме и определяет поведение в случае ошибок кодирования или декодирования
newline - Отвечает за преобразование окончание строки
closefd -Указывает оставлять ли файловые дескрипторы открытым при закрытии файла
opener - Позволяет передать пользовательскую функцию для открытия файла
'''

#f = open('data.txt', 'wb')
#f.write('ПломбиР, '.encode('utf-8') + "мир!".encode('cp1251') )
#f.close()

f = open('data.txt', 'r', encoding='utf-8') 

'''print(list(f)) 
          ^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 16: invalid continuation byte'''


#print(list(f)) 
#f.close()

f= open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()
