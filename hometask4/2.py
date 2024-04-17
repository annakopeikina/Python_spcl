#2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
#используйте его строковое представление.

def keyword_args_to_dict(**kwargs) -> dict:
    """
    Функция принимает только ключевые параметры и возвращает словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента.
    Если ключ не хешируем, используется его строковое представление.
    """
    result = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, complex, tuple, list, dict, set, frozenset)): #Проверяет на хешируемость, и, 
            key = str(key)                                                                                  #если  не хешируемый, заменяет на str
        if isinstance(value, (int, float, complex, tuple, list, dict, set, frozenset)):
            value = str(value)
        result[value] = key
    return result

if __name__ == '__main__':
    # Пример использования функции
    args_dict = keyword_args_to_dict(a=888, b='yellow', c=[2, 4, 3])
    print(args_dict)
