from genericpath import exists
from importlib.resources import path
from pathlib import Path
from random import randint
from unicodedata import name
from posixpath import dirname
from pydoc import pathdirs


# def generateFiles(dir):
#     Path(dir).mkdir(exist_ok=True)
#     for i in range(15):
#         Path(f'{dir}/'
#             f'{randint(2020, 2022)}-'
#             f'{randint(1,12)}-'
#             f'{randint(1,31)}.txt'
#         ).touch()

# generateFiles('/Users/ekaterina/generated_files2')  

def generate_tree(dir_name,level=0):

    dir_path = Path(dir_name)
    
    print('|','   |'*level,'_', dir_path.name)
    for item_path in dir_path.iterdir():
        if item_path.is_file():
            print('|','   |'*level,' ','|__', item_path.name)
        else:
            generate_tree(item_path, level=level+1)
    
    print('|','   |'*level)


def restructure_directory(dir_name) ->str:
    dir_path = Path(dir_name)
    for file_path in dir_path.iterdir():
        
        if file_path.is_dir():
            continue

        #print(file_path)

        new_name = (file_path.name).replace("-", "/")
        new_file_path = Path(file_path.parent, new_name)

        new_file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.replace(new_file_path)   


if __name__ == '__main__':

    restructure_directory('/Users/ekaterina/generated_files2')
    generate_tree('/Users/ekaterina/generated_files2')

    
