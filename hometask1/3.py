"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint 
LOWER_LIMIT=1
UPPER_LIMIT=99
MAX_ATTEMPTS=10

number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Программа загадала число от", LOWER_LIMIT, "до", UPPER_LIMIT, ".У вас есть", MAX_ATTEMPTS,"попыток5,чтобы угадать его")

for attempt in range(1, MAX_ATTEMPTS+1):
    try:
        guess = int(input(f"Попытка №{attempt}: Введите ваше предположение: "))
    except ValueError:
        print("Не угадали. Попробуйте снова.")
        continue

    if guess == number:
        print(f"Вау! Вы угадали число {number} за {attempt} попыток.")
        break

    elif guess < number:
        print("Загаданное число больше вашего предположения.")
    else:
        print("Загаданное число меньше вашего предположения.")
else:
    print("Это была последняя попытка; загаданное число: ", number)



        
