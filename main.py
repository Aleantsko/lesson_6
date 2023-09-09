# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def geometric_progression(first_number, step, count):
#     if count == 0:
#         return 0
#     answer.append(first_number)
#     print(first_number)
#     count -= 1
#     return geometric_progression(first_number + step, step, count)
#
#
# a1 = int(input('Enter first number: '))
# step = int(input('Enter step: '))
# count = int(input('Enter count: '))
# answer = []
# geometric_progression(a1, step, count)
# print(answer)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

min = int(input('Enter min: '))
max = int(input('Enter max: '))
list = []
for i in range(20):
    list.append(random.randint(-10, 10))

print(list)
answer = []

for num in list:
    if min < num < max:
        answer.append(num)
        
print(answer)
