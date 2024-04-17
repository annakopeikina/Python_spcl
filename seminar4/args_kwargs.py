'''
*args and **kwargs могут возвращать несколько значений
def func(*args): - принимает любое число позиционных аргументов
def func(**kwargs): - принимает любое число ключевых аргументов
def func(*args, **kwargs): -принимает любое число позиционных и ключевых аргументов

'''
def school_print(**kwargs): 
    for key, value in kwargs.items():
    
        print(f'По предмету "{key}" получена оценка {value}')

school_print(химия=5, физика=4, математика=5, физкультура=5)
