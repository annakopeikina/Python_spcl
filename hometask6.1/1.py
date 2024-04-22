from datetime import datetime as dt
from calendar import isleap
import sys

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        year = t.year
        if isleap(year):
            print(f'{year} год - високосный')
        else:
            print(f'{year} год - не високосный')
        return True
    except ValueError:
        print("Неправильный формат даты. Используйте формат dd.mm.yyyy")
        return False

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Используйте команду в следующем формате: python hometask6.1\1.py дд.мм.гггг")
    else:
        date_to_check = sys.argv[1]
        check_date(date_to_check)


