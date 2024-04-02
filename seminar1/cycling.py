number = float(input('Введите число: '))
count= 0
while count < number:
    print(count)
    count += 2


number = float(input('Введите число: '))
STEP = 2
limit = number - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0: 
        continue

    print(count)


min_limit = 0
max_limit = 10
while True:
    print('Введите число между', min_limit,'и', max_limit,  '? ')
    number = float(input())
    if number < min_limit or number > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число ', number)
    
    
    
    
    
    
    
