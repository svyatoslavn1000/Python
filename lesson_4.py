# #Execize 1
#
# from sys import argv
#
# script_name, count_hours, rate,  bonus = argv
# a = int(count_hours)
# b = int(rate)
# c = int(bonus)
# salary = a * b + c
# print(salary)
#
# # Команда в директории с файлом  lesson_4.py
# # python3 lesson_4.py 170 300 5000

# #Execize 2
# import random
# capacity = 10
# example = [random.randint(0, 20) for el in range(capacity) ]
# generated = []
#
# for i in range(len(example)-2):
#     if example[i] < example[i+1]:
#         generated.append(example[i+1])
# print(example)
# print(generated)

# #Execize 3
# # Самоочевидно, таких чисел нет: ближайшее 420
#
# print([num for num in range(20, 240) if num % 20 == 0 and num % 21 == 0 ])

# #Execize 4
# # Сдаюсь! Последней надеждой была рекурсия генератора [number for number in example if number not in unique]
# import random
#
# capacity = 10
# unique_2 = []
# example = [random.randint(0, 20) for el in range(capacity)]
# unique_1 = list(set(example))
# for number in example:
#         if number in unique_2:
#             continue
#         else:
#             unique_2.append(number)
# print(example)
# print(unique_1)
# print(unique_2)
# # кстати, ответы разные

# #Execize 5
# from functools import reduce
#
# initial = [el for el in range(100, 1000) if el % 2 == 0]
# mult_all = reduce(lambda x, y: x * y, initial)
#
# print(mult_all)

## Execize 6
# from itertools import count
# from itertools import cycle
#
# min =1
# max = 20
# c = 0
# list = [2, 4, 8, 5, 37, 4, 6, 17, 25, 84]
# for i in count(min):
#     if i > max:
#         break
#     else:
#         print(i)
#
# for item in cycle(list):
#     if c > 2:
#         break
#     print(item)
#     c += 1

# # Execize 7
# num = 10
# def fact(n):
#     a = 1
#     for x in range(1, n):
#         a = a * x
#         yield a
#
# b = [el for el in fact(num)]
# print(b)