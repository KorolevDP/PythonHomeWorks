# -*- coding: cp1251 -*-

'''

���������� ������� ��������� ������� (������), �������� ������� ����������� ��������� ��������� 
(�.�. �� ������ ��������� �������� � �� ������ ��������� ���������).

'''

from array import array
from random import randint

min_value = int(input("Enter minimum of range:> "))
max_value = int(input("Enter maximum of range:> "))

user_array = array('i',[])
index_array = array('i',[])

for i in range(15):
    i = randint(1, 25)
    user_array.append(i)


for j in range(len(user_array)):
    if min_value <= user_array[j] <= max_value:
        index_array.append(j)

print(list(user_array))
print("====================================================================")
print("Indexes of elements from a range:>" , list(index_array))