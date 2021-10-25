"""

Создание папки (с указанием имени); #DONE
Удаление папки по имени; #DONE
Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх; #done
Создание пустых файлов с указанием имени; #DONE
Запись текста в файл; #DONE
Просмотр содержимого текстового файла; #DONE
Удаление файлов по имени; #DONE
Копирование файлов из одной папки в другую; #DONE
Перемещение файлов; #DONE
Переименование файлов. #DONE


"""

"""C O D I N G  C H A P T E R"""
import sys, os, shutil

def create_file(name, text=None):
    with open(name, 'w',encoding='utf-8') as file:
        if text:
            file.write(text)
def delete_file(name):
    try:
        os.remove(name)
    except:
        print('Невозможно удалить папку этой командой')
def move_btw_dir(path):
    from importlib import reload
    reload(os)
    os.chdir(path)
    #path()
def create_dir(name):
    try:
        os.mkdir(name)
    except:
        print(f'Невозможно создать файл, так как он уже существует: {name}')

def path():
    print(os.getcwd())
    res=os.getcwd()
    return res


def checkfile(name):
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
def delete_dir(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
    except OSError:
        print('папка должна быть пустой')
    #except
def copy_file(path_to_file,path):
    try:
        shutil.copy(path_to_file,path)
    except:
        print("can't copy")
def move_file(path,new_path):
    try:
        shutil.move(path,new_path)
    except:
        print("can't move")
def renamer(name,new_name):
    try:
        os.rename(name,new_name)
    except:
        print(f'Невозможно создать файл, так как он уже существует: {name} -> {new_name}')

def write_help():
    print("1. - создание файла ")
    print("2. - запись в файл ")
    print("3. - удаление файла ")
    print("4. - перемещение между папками")
    print("5. - создание папки")
    print("6. - показать текущий путь")
    print("7. - прочитать файл")
    print("8. - удалить папку")
    print("9. - скопировать файл")
    print("10. - переместить файл")
    print("11. - переименовать файл")
    print('напишите exit для выхода. ')
    print("12. - вызвать справку")

def start_prog():
    write_help()
    while True:
        command = input('Введите команду: ')
        if command == '1':
            name = input('Введите имя файла: ')
            create_file(name)
        if command == '2':
            name = input('Введите имя файла: ')
            text = input('Введите текст файла: ')
            create_file(name, text)
        if command == '3':
            name = input('Введите имя файла: ')
            delete_file(name)
        if command == '4':
            ppath = input('Введите полный путь до папки: ')
            move_btw_dir(ppath)
        if command == '5':
            name = input('введите имя папки: ')
            create_dir(name)
        if command == '6':
            path()
        if command == '7':
            name = input('введите имя файла: ')
            checkfile(name)
        if command == '8':
            name = input('введите имя файла: ')
            delete_dir(name)
        if command == '9':
            ppath, new_path = input('введите путь до файла: '), input('введите новый путь: ')
            copy_file(ppath, new_path)
        if command == '10':
            ppath, new_path = input('введите путь до файла: '), input('введите новый путь: ')
            move_file(ppath,new_path)
        if command == '11':
            name,new_name=input('введите имя файла: '),input('введите новое имя файла:')
            renamer(name,new_name)
        if command == '12':
            write_help()
        if command == 'exit':
            break


"""C O D I N G  C H A P T E R"""



"""T E S T I N G   C H A P T E R"""
#create_file('newf.txt','usedonce')
#checkfile('newf.txt')
#renamer('newf.txt','not_newf.txt')
#create_dir('what')
#delete_dir('what')
#delete_file('what')
#path()
#move_btw_dir()
start_prog()
"""T E S T I N G   C H A P T E R"""