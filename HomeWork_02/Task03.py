# -*- coding: cp1251 -*-

'''

Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Пример:

Input: 10

Output:1,2,4,8

'''

from math import pow

number = int(input("Enter number:> "))

for i in range(number):
    power = pow(2,i)
    if(power <= number):
        print("%.0f" %power)                