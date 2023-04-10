# -*- coding: cp1251 -*-

'''

Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 

'''

number = int(input("Enter number:> "))
result = 0

while number > 0:

     result += number % 10
     number //= 10

print(f" {number} --> {result}")