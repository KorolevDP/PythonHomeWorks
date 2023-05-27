# -*- coding: cp1251 -*-

'''

1. Открывать файл (режим txt)
2. Сохранить файл
3. Показать все контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход

'''
        
def open_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        data = [line.rstrip() for line in file]
        return data   

def write_in_file(file_path):
    with open(file_path, 'w') as file_:
        file_.writelines("%s" % i for i in data)
        
def assign_id_for_contacts(data):
    number_list = list(enumerate(data, 1))
    for i in number_list:
        print(*i)
        print()

def show_all_contacts(data):   
    for i in data: 
        print(i)
        
def add_contact(data):
    new_name = input("Введите имя для добавления:> ")
    new_tel = input("Введите телефон для добавления:> ")
    new_comment = input("Введите комментарий для добавления:> ")
    data.append(new_name + '; ' + new_tel + '; ' + new_comment)
    return data
 
def search_contact(data):
    flag = 1
    text_for_find = input("Введите атрибут для поиска контакта:> ")
    for item in data:
        if text_for_find in item:
            flag = 0
            print(item)
    if flag: print("\033[3m\033[33m\033[41m{}\033[0m".format("Ошибка! Данные не найдены!"))

def delete_contact(data):
     assign_id_for_contacts(data)
     id_contact = int(input("Введите id контакта для удаления:> ")) - 1
     del data[id_contact]
    
def change_contact(data):
    assign_id_for_contacts(data)
    id_contact = int(input("Введите id для изменения контакта:> ")) - 1
    contact_for_changes = data[id_contact]
    print(contact_for_changes)
    
def exit_(f):
    return exit()

file_path = "catalog.txt"
data = open_file(file_path)

dict_command = {
                '1': write_in_file, 
                '2': show_all_contacts,
                '3': add_contact,
                '4': search_contact,
                '5': change_contact,
                '6': delete_contact,
                '7': exit_
                }

print()
print("\033[4m\033[30m\033[43m{}\033[0m".format("Меню:"))
options = ['1. Сохранить файл', 
           '2. Показать все контакты',
           '3. Добавить контакт', 
           '4. Найти контакт', 
           '5. Изменить контакт', 
           '6. Удалить контакт', 
           '7. Выход']
print(*options, sep = '\n')
print()

while True:   
    print()
    command_ = input("Выберите пункт из меню:> ")
    print()
    if command_ in dict_command:
        dict_command[command_](data)
    else:
         print("\033[3m\033[33m\033[41m{}\033[0m".format("Ошибка! Некорректная команда!"))