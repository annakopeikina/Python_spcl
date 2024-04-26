# как находить файлы, узнавать, что каталог, что файл ; перемещаться по файлу, по папкам, углубляться в директорию и рекурсивно обращаться

import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

p= Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')

'''
print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
'''