import os

# Создаем директорию 'other_dir'
os.makedirs('dir/other_dir')

# Создаем директорию 'some_dir'
os.makedirs('some_dir')

import shutil # для масштабных манипуляций

shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')

from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

## потренироваться в новом файле
#shutil.copy('one.txt', 'dir')
#shutil.copy2('two.txt', 'dir/one_more')

shutil.rmtree('dir')  # удаляет файлы директории папки

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
