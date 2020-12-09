# #Execize 1
#
# def func_division():
#     print("Bедите делимое: ")
#     a = int(input())
#     print("Bедите делитель: ")
#     b = int(input())
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("func_division: Деление на ноль невозможно.")
#
# a = func_division()
# print(a)
#
# #Exescize 2
#
# def print_user_data(name, surname, year_of_birth, city, email, phone):
#     print(f"{name}, {surname}, {year_of_birth}, {city}, {email}, {phone}")
#
# print_user_data("Bob", "Bobson", "1999", "Los-Alamos", "bob@gmail.com", 5555555)
#
# #Exescize 3

# def my_func(a, b, c):
#     if(a > c and b > c):
#         return a + b
#     elif(a > b and c > b):
#         return a + c
#     else:
#         return b + c
# print(my_func(1,-3,5))

# #Exescize 4
#
# def rase_to_negative_degree1(base, power):
#     a = - power
#     x = 1
#     while a > 0:
#         x = x / base
#         a -= 1
#     return x
#
# def rase_to_negative_degree2(base, power):
#     return base ** power
#
# print(rase_to_negative_degree1(2, -3))
# print(rase_to_negative_degree2(2, -3))

# #Exescize 5
#
# def sum():
#     initial_sum = 0
#     stop = True
#     while stop:
#         print("Введите числа через запятую и нажмите ввод:")
#         a = input()
#         numbers = a.split(',')
#         for number in numbers:
#             if(number.isdigit()):
#                 initial_sum += int(number)
#             else:
#                 stop = False
#                 break
#         print(initial_sum)
#     return initial_sum;
#
# b = sum()
# print(b)

# #Exescize 6
#
# def int_func(str):
#     return str.capitalize()
# 
# def up_str(str):
#     strings = str.split(' ')
#     new_str = ""
#     for string in strings:
#         string = int_func(string)
#         new_str = f"{new_str} {string}"
#     return new_str.strip()
#
# print(int_func("water"))
# print(up_str("мама мыла раму"))