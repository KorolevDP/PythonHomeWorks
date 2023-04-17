
'''
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X.

5
1 2 3 4 5
3 -> 1

'''
from random import randint

size_list = int(input("Enter size of list:> "))
my_list = [randint(1, 10) for x in range(size_list)]
count = 0
print(my_list)
number = int(input("Enter number from list:> "))

for i in range(len(my_list)):
	if number == my_list[i]:
		count += 1

print(f"{number} appears in the list {count} times")