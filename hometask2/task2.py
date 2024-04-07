#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction
numerator1 = int(input("Введите числитель первой дроби: "))
denominator1 = int(input("Введите знаменатель первой дроби: "))

numerator2 = int(input("Введите числитель второй дроби: "))
denominator2 = int(input("Введите знаменатель второй дроби: "))

def add_fractions(fraction1, fraction2):
    # Находим общий знаменатель
    common_denominator = fraction1[1] * fraction2[1]
    
    # Приводим дроби к общему знаменателю и складываем числители
    sum_numerator = fraction1[0] * (common_denominator // fraction1[1]) + fraction2[0] * (common_denominator // fraction2[1])

    return sum_numerator, common_denominator

def multiply_fractions(fraction1, fraction2):
    product_numerator = fraction1[0] * fraction2[0]
    product_denominator = fraction1[1] * fraction2[1]
    
    return product_numerator, product_denominator

sum_result = add_fractions((numerator1, denominator1), (numerator2, denominator2))

product_result = multiply_fractions((numerator1, denominator1), (numerator2, denominator2))

print("Сумма дробей:", f"{sum_result[0]}/{sum_result[1]}")
print("Произведение дробей:", f"{product_result[0]}/{product_result[1]}")

# Проверка с модулем Fraction
from fractions import Fraction

def operate_fractions(fraction1, fraction2):
    # Преобразование строк в дроби
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)
    
    sum_result = frac1 + frac2
    product_result = frac1 * frac2
    
    return sum_result, product_result

fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

sum_result, product_result = operate_fractions(fraction1, fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)

