import random as rnd
from sys import builtin_module_names as bmn, path as p 


print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6)) # если создать одноименный имеющемуся модуль, нужно добавить name_ (нижнее подчеркивание) во избежание конфликта
'''print(path)
print(sys.path)'''