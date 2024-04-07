import sys #import зарезервированное слово

STEP = 2**16 
num = 1
for _ in range(30): #подчеркивание= переменная не нужна
    print(sys.getsizeof(num), num) 
    num *= STEP
num =765_345_325 #удобнее смотреть число
print(num)