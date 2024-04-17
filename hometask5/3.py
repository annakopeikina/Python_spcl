# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    """
    Генератор чисел Фибоначчи.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_generation = fibonacci_generator()
for _ in range(8):
    print(next(fibonacci_generation))
