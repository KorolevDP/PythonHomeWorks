# -*- coding: cp1251 -*-

'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*

2, 2 --> 4 

'''

def sum_of_numbers (first_num, second_num):
    if first_num == 0:
       return second_num
    elif second_num == 0:
       return first_num
    else:
        return sum_of_numbers(first_num + 1, second_num - 1)

first_num = int(input("Enter first number:> "))
second_num = int(input("Enter second number:> "))

print(f"Summ of numbers = {sum_of_numbers(first_num, second_num)}")