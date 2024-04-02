color = input('цвет пламени: ')
match color:
    case 'красный' | 'оранжевый':
        print('Sr, Li, Ca, Ra')
    case 'зеленый':
        print('Ba, Cu, B')
    case 'синий' | 'голубой':
        print('In, As, Se, Cs')
    case 'желтый':
        print('Fe, Na')
    case _:
        print('Определите точнее')
        
