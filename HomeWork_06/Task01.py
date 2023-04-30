# -*- coding: cp1251 -*-

'''

Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

'''

from array import array

first_elem = int(input("Enter first element of an arithmetic progression:> "))
difference = int(input("Enter difference elements of an arithmetic progression:> "))
amount_of_elements = int(input("Enter аmount of elements of an arithmetic progression:> "))
elem_of_aritm_progression = array('i',[] )

current_element = 0
for i in range (amount_of_elements):
    current_element = first_elem + i * difference
    elem_of_aritm_progression.append(current_element)
   
print(list(elem_of_aritm_progression))