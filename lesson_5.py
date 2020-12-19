#Execize 1
# Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных
# свидетельствует пустая строка.
#
# with open("text.txt", "a+") as out_f:
#     print("Введите строку: ")
#     line = input()
#     out_f.write(f"{line}\n")
#     while line != '':
#         print("Введите строку: ")
#         line = input()
#         out_f.write(f"{line}\n")
# print("END")

# #Execize 2
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
# # "Словом считается любой набор символов между пробелами,
# исключая знаки препинания и некоторые символы.

# bad_chars = [';', ':', '!', "*", "?", "/", ".", ","]
# with open("text.txt", "r") as in_f:
#     number_lines = 0
#     number_words = []
#     for line in in_f:
#         for i in bad_chars:
#             line = line.replace(i, '')
#         number_lines += 1
#         words = line.split(" ")
#         number_words.append(len(words))
# print(f"В файле {number_lines} строк, число слов в строках {number_words}")

#Execize 3
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# При решении считается, что фамилия отделена от зарплаты пробелом
# зарплата стоит в конце списка.
# def personal(line):
#     word_list = line.split()
#     person = []
#     for word in word_list:
#         if word.isnumeric():
#             person.append(int(word))
#         else:
#             person.append(word)
#     return person
#
# min_salary = 20000
# with open("text.txt", "r") as in_f:
#     list = []
#     sum = 0
#     count = 0
#     for line in in_f:
#         salary = personal(line)[-1]
#         sum += salary
#         count += 1
#         if salary < min_salary:
#              list.append(personal(line)[0:-1:])
# avarage = sum/count
# print(*list, f"Средняя зарплата {avarage}")

# #Execize 4
# ru = ["Один", "Два", "Три", "Четыре"]
# words = []
# with open("count.txt", "r") as in_f:
#     i = 0
#     for line in in_f:
#         words = line.split(" ")
#         words.pop(0)
#         words.insert(0, ru[i])
#         i += 1
#         with open("count_ru.txt", "a+") as out_f:
#             out_f.write(' '.join(words))

# #Execize 5
# Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

# def create_f(str):
#     with open(str, "a+") as out_f:
#          for i in range(1, 100):
#              out_f.write(f"{2*i} ")
#
# def sum_in_f(str):
#     with open(str, "r") as in_f:
#         for line in in_f:
#             numbers = line.split(" ")
#             sum = 0
#             for n in numbers:
#                 if n.isnumeric():
#                     sum += int(n)
#     return sum
# create_f("numbers.txt")
# print(sum_in_f("numbers.txt"))


# #Execize 6
# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие л
# екционных, практических и лабораторных занятий
# по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# def exstract_numbers(str):
#     l = len(str)
#     integ = []
#     i = 0
#     while i < l:
#         s_int = ""
#         a = str[i]
#         while "0" <= a <= "9":
#             s_int += a
#             i += 1
#             if i < l:
#                 a = str[i]
#             else:
#                 break
#         i += 1
#         if s_int != '':
#             integ.append(int(s_int))
#     return integ
#
# def hours(str):
#     dict_sp = {}
#     with open(str, "r") as in_f:
#         for line in in_f:
#             tokens = line.split(":")
#             list_hours = exstract_numbers(line)
#             s = sum(list_hours, 0)
#             dict_sp[tokens[0]] = s
#     return dict_sp
#
# print(hours("plan.txt"))

# #Execize 7

str = "spisok.txt"
import json
name = 0
type = 1
pr = 2
lo = 3
info_ditionary = {}
with open(str, "r") as in_f:
    sum = 0
    for line in in_f:
        list_inf = line.split(" ")
        name_firm = list_inf[name]
        debet = int(list_inf[pr])
        loss = int(list_inf[lo])
        profit = debet - loss
        if profit >= 0:
            sum += profit
        else:
            continue
        info_ditionary[name_firm] = profit

list_info =[info_ditionary, {"average_profit": sum}]
result_json = json.dumps(list_info)
print(result_json)