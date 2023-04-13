# -*- coding: cp1251 -*-

'''

На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

Input: 5 -> 1 0 1 1 0

Output: 2

'''

import random

number_of_coins = int(input("Enter number of coins:> "))
sides_of_coins = [random.randint(0,1) for i in range(number_of_coins)]
count_eagles = 0
count_tails = 0

print("Sides of coins: ", sides_of_coins)

for i in sides_of_coins:
    if i == 1:
       count_eagles += 1 
    else:
        count_tails += 1

if count_tails == count_eagles:
    print(f"Minimum number of coins to flip = {count_tails} ")
elif count_tails < count_eagles:
    print(f"Minimum number of coins to flip = {count_tails}")
else:
    print(f"Minimum number of coins to flip = {count_eagles}")