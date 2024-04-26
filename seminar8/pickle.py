#модуль PICKLE

import pickle # преобразует данные в байты, не проверяя на безопасность
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Karma Comma'\ntR)")
print(f'{res = }')

os.system("echo " + res)

# None, True, False
# int, float, complex;
# str, bytes, butearrays;
# tuple, list, set, dict 
# lambda

import pickle
pickle.dump('''my_dic, f''')

