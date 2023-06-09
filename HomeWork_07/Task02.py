# -*- coding: cp1251 -*-

'''
�������� ������� print_operation_table(operation, num_rows=6, num_columns=6), 
������� ��������� � �������� ��������� �������, ����������� ������� �� ������ ������ � �������.
��������� num_rows � num_columns ��������� ����� ����� � �������� �������, ������� ������ ���� �����������. 
��������� ����� � �������� ���� � ������� (���������, ������ �� � ����). 
����������: �������� ��������� ���������� ����� ��������, � ������� ����� ��� ���������, ���, ��������, � �������� ���������.

*������:*

**����:** `print_operation_table(lambda x, y: x * y) ` 
**�����:**

1   2   3   4   5   6
2   4   6   8   10  12
3   6   9   12  15  18
4   8   12  16  20  24
5   10  15  20  25  30
6   12  18  24  30  36

'''

def print_operation_table(operation, num_rows, num_columns):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            print(operation(row, col), end = '\t')
        print()

print_operation_table(lambda x,y: x * y, 5,5)