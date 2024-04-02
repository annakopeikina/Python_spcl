#Посчитайте сумму чётных элементов от 1 до n исключая кратные e.Используйте while и if.
 # Попробуйте разные значения e и n.

n = int(input("Введите число: "))
e = int(input("e: "))
count = 2
summ = 0
while count <= n:
    if count % e == 0:
        count +=2
        continue 
    summ += count
    count +=2
    print(summ)
print(" ")    
print(summ)