# directory
import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')  # подимается на одну директорию выше к родительской папке
print(os.getcwd())
print(Path.cwd())  

os.mkdir('new_os_dir')
#Path('new_path_dir').mkdir(parents=True)
Path('some_dir/dir/new_path_dir').mkdir(parents=True)



