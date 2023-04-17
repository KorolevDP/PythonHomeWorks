
'''
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai.
Последняя строкасодержит число X

5
1 2 3 4 5
6 -> 5

'''

from random import randint

size_list = int(input("Enter size of list:> "))
my_list = [randint(1, 20) for x in range(size_list)]
my_list = list(set(my_list))
print(my_list)
number = int(input("Enter a number close to the number from the list:> "))

for i in range(len(my_list)):
	if number == my_list[i] or number == my_list[i] + 1 or number == my_list[i] - 1:
		print(f"Close number for {number} ---> {my_list[i]}")
		