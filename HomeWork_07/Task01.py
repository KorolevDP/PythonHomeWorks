# -*- coding: cp1251 -*-

'''
�����-��� �������� ��� ����������, ���� �� � ��� ������ ����. 
��������� ����������� � ��� ��������� �� ��������� ������, ��������� ����� �� �� �����������, ��� ����� �������� ���������. 
�����-��� �������, ��� ���� ����, ���� ����� ������ (�.�. ����� ������� ����) � ������ ����� ������������� ����������.
����� ����� �������� �� ������ �����, ���� �� ����� ��������� ����, �� ��� ����������� ��������. 
����� ���������� ���� �� ����� ���������. �������������  �����-��� ������� � ��������� � ����������. 
� ������ �������� ������ ���-���, ���� � ������ ��� � ������� � ���� �����, ���� � ������ ��� �� � �������

*������:*

**����:** ����-��-��� ���-���-����� ��-��-��-��    
**�����:** ����� ���-���  

'''

poem = input("Enter your poem:> ")
phrases = poem.split()

number_of_vowels = [sum(x in '���������' for x in word) for word in phrases]

if len(set(number_of_vowels)) == 1:
    output_ = "����� ���-���"
else: output_ = "��� �����"

print(output_)