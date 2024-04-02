min_limit = 0
max_limit = 10
count =3
number = None

while count > 0:
    print("Попытка ", count)
    count -= 1


    print("Введите число между", min_limit, 'и', max_limit, "? ")
    number = float(input())
    if number < min_limit or number > max_limit:
        print("Неверно")
    else:
        break

else:
    print("Исчерпаны все попытки")
    quit()
print("Было введено число ", number)
