import os
from pathlib import Path
from pprint import pprint
import shutil

print(os.getcwd())
print(Path.cwd())

print(os.path.exists('d:\VS_code\My-Vscode-Project\demofile.txt'))
print(Path('d:\VS_code\My-Vscode-Project\demofile.txt').exists())
print(Path('.\My-Vscode-Project\demofile.txt').exists())

file_list = list(Path('d:\VS_code\My-Vscode-Project').glob('*.py'))
print(file_list)
for file in file_list:
    print(file.name)
    print(file)
    # with open (file, 'r', encoding='utf-8') as f:
    #     print(f.read())

print(os.listdir('d:\VS_code\My-Vscode-Project'))
print(os.path.abspath('d:\VS_code\My-Vscode-Project'))

print("###############################")

f = open('d:\VS_code\My-Vscode-Project\demofile.txt', 'r+', encoding='utf-8')

# print(f.read())

# for line in f:
#     print(line, end='')

L = f.readlines()
L[1] = 'This is line 3\n'
print(L)
f.seek(0)
f.truncate()
print(f.read())
f.writelines(L)
f.seek(0)
print(f.read())
f.close()

print(dir(shutil))
shutil.copy('d:\VS_code\My-Vscode-Project\demofile.txt', 'd:\VS_code\My-Vscode-Project\demofile_copy.txt')
shutil.move('d:\VS_code\My-Vscode-Project\demofile_copy.txt', 'd:\VS_code\My-Vscode-Project\demofile_copy_moved.txt')

with open('d:\VS_code\My-Vscode-Project\demofile.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        print(i, line, end='')

if os.path.exists('d:\VS_code\My-Vscode-Project\demofile_copy_moved.txt'):
    os.remove('d:\VS_code\My-Vscode-Project\demofile_copy_moved.txt')
    print('\nFile deleted')
