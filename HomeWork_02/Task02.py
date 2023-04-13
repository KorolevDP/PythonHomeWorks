'''

 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
 Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
 Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

 Пример:

 Input: 7,10

 Output: 2,5

'''

product = int(input("Enter product number:> "))
sum_numbers = int(input("Enter sum number:> "))

for first_num in range(sum_numbers):
    for second_num in range(product):
        if sum_numbers == first_num  + second_num and product == first_num  * second_num:
             print(f"First number -->{first_num}\nSecond number -->{second_num}")   
   

