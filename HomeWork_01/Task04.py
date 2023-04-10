
'''

 Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой между
дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no

'''

length = int(input("Enter length of chocolate:> "))
width = int(input("Enter width of chocolate:> "))
numberOfSlices = int(input("Enter number of slices chocolate:> "))

if numberOfSlices < length * width and ((numberOfSlices % length == 0)) or ((numberOfSlices % width == 0)):
    print(f"{length}, {width}, {numberOfSlices} ---> YES")
else:
    print(f"{length}, {width}, {numberOfSlices} ---> NO")
