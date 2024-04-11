#_______________split-разбивание на строки
link = 'http://habr.com/ru/users/pjero/posts/' 
urls = link.split('/')
print(urls)
urls_joined = " ".join(urls)
print(urls_joined)

a, b, c = input('введите 3 числа через пробел: ').split()
print(c,b,a)

a, b, c, *_ = input('введите не менее трёх чисел через пробел: ').split()

