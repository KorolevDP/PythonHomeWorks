# -*- coding: cp1251 -*-

main_menu = '''\n������� ����:
    1. ������� ����
    2. ��������� ����
    3. �������� ��������
    4. �������� �������
    5. ����� �������
    6. �������� �������
    7. ������� �������
    8. �����\n'''

input_choice = '�������� ����� ����: '

load_successful = '���������� ����� ������� �������'

save_successful = '���������� ����� ������� ���������'

pb_empty = '���������� ����� ����� ��� �� ���������'

input_new_contact = '������� ������ ������ ��������:'

new_contact = {'name': '������� ���: ', 
               'phone': '������� ����� ��������: ', 
               'comment': '������� �����������: '}

def new_contact_successfull(name: str):
    return f'������� {name} ������� ��������'

input_search = "������� �������� �������� ��� ������: "

def empty_search(word) -> str:
    return f'�������� ���������� ����� "{word}" �� �������'

input_change = "����� ������� ����� ������: "
input_index = "������� ������ ��������: "

change_contact = '������� ����� ������ ��� �������� ���� ������, ����� �� ������: '

def change_succsessful(name: str) -> str:
    return f'������� {name}������� �������'

input_delete = "����� ������� ����� �������: "

def delete_succsessful(name: str) -> str:
    return f'������� {name} ������� ������'
