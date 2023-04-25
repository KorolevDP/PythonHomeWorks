'''

Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 

'''

def power_of_number (num, pow):
    if pow == 0: return 1
    return num * power_of_number(num, pow -1)

number = int(input("Enter number:> "))
power = int(input("Enter power of number:> "))

print(f"Number {number} in power {power} = {power_of_number(number, power)}")