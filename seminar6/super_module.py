from random import randint

SIZE = 100 # (глобальная переменная)
_secret ='qwerty' # "_name"- защищенная переменная  (глобальная переменная) при импорте через * не импортируются
__top_secret = '1q2w3e4r5t6y'# "__name" - приватная переменная (глобальная переменная) при импорте через * не импортируются

def func(a: int, b: int) -> str:
    z = f'в диапазоне от {a} до {b} получили {randint(a, b)}'
    return z

result = func(1,6)

