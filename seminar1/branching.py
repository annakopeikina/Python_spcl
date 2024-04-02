password_detect = 'Y'
result = input('Input password: ')
if result == password_detect:
    print('Доступ разрешен')
    my_math = int(input('2 * 2 = '))
    if 2*2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Не забудьте закрыть за собой дверь')
else:
    print('Доступ запрещен')
print('Работа завершена')    
