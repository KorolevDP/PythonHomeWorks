# -*- coding: cp1251 -*-

'''

��������� ������ ���������� �������������� ����������. 
Ÿ ������ �������, �������� � ���������� ��������� ����� ������ � ����������. 
������� ��� ��������� n-�� ����� ����������: an = a1 + (n-1) * d.
������ ����� �������� � ����� ������.

'''

from array import array

first_elem = int(input("Enter first element of an arithmetic progression:> "))
difference = int(input("Enter difference elements of an arithmetic progression:> "))
amount_of_elements = int(input("Enter �mount of elements of an arithmetic progression:> "))
elem_of_aritm_progression = array('i',[] )

current_element = 0
for i in range (amount_of_elements):
    current_element = first_elem + i * difference
    elem_of_aritm_progression.append(current_element)
   
print(list(elem_of_aritm_progression))