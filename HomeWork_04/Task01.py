# -*- coding: cp1251 -*-

'''
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 
6

2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

---> 6 12

'''

from random import  randint

size_first_list, size_second_list = (int(input(f"Enter {i+1} list size:> ")) for i in range(2))

first_list = [randint(1, 25) for _ in range(size_first_list)]
second_list = [randint(1, 25) for _ in range(size_second_list)]
result = set(first_list) & set(second_list)
sorted(result)

print()
print("first list -->", first_list)
print("second list -->",second_list)
print("Сommon numbers for the first and second lists -->",result)