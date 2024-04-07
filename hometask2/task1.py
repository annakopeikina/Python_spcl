#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

def to_hexadecimal(num):
    hexadecimal_str = hex(num)
    return hexadecimal_str

number = input("Введите целое число: ")

if number.isdigit():
    number = int(number)
    hexadecimal_representation = to_hexadecimal(number)
    
    print("Шестнадцатеричное представление числа:", hexadecimal_representation)
    
    # Проверка результата с использованием встроенной функции hex()
    print("Проверка с использованием hex:", hex(number))
else:
    print("Ошибка: Введено не целое число или не число!")
