# Execize 1
# class Date:
#
#     def __init__(self, date):
#         self.date = date
#
#     @classmethod
#     def date_to_number(cls, date):
#         list = date.split("-")
#         str = f"{list[0]}{list[1]}{list[2]}"
#         return int(str)
#
#     @staticmethod
#     def validate_of_date(date):
#         str1 = "Неверное значение числа месяца"
#         str2 = "Некорректный формат даты"
#         str3 = "Неверное значение месяца"
#         list = date.split("-")
#         if int(list[1]) < 0 | int(list[1]) > 12:
#             return str3
#
#         if int(list[0]) < 0:
#             return str2
#
#         if int(list[1]) == 1 | int(list[1]) == 3 | int(list[1]) == 5 \
#                 | int(list[1]) == 7 | int(list[1]) == 8 | int(list[1]) == 10 | int(list[1]) == 12:
#             if int(list[0]) > 31:
#                 return str1
#         elif int(list[1]) == 4 | int(list[1]) == 6 | int(list[1]) == 9 \
#                 | int(list[1]) == 11:
#             if int(list[0]) > 30:
#                 return str1
#         elif int(list[1]) == 2:
#             if list[2] % 4 == 0:
#                 if int(list[0]) > 29:
#                     return str1
#             else:
#                 if int(list[0]) < 0 | int(list[0]) > 28:
#                     return str1
#         else:
#              return  "200"
#
#
# print(Date.date_to_number("23-12-2021"))
# print(Date.validate_of_date("31-12-2015"))

# Execize 2
#
# class OwnError(ZeroDivisionError):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# grants = 0
# self = 0
# while True:
#     inp_data_incubus = input("Введите дЕЛИМОЕ: ")
#
#     inp_data_supptibus = input("Введите Делитель: ")
#
#     try:
#         inp_data_supptibus = int(inp_data_supptibus)
#         inp_data_incubus = int(inp_data_incubus)
#         if inp_data_supptibus == 0:
#             raise OwnError("Вы ввели отсутствующего Делителя и лишены возможности Делить!")
#     except ValueError:
#          print("Вы ввели не число")
#     except OwnError as err:
#         print(err)
#         break
#     else:
#           grants += inp_data_incubus // inp_data_supptibus
#           self += inp_data_incubus % inp_data_supptibus
#
#           print(f"Вы хорошо делите. У Делителя {grants} У вас: {self} супптибусов.")

# Execize 3

# class MyError(ValueError):
#     def __init__(self, txt):
#         self.txt = txt
#
# inp_data = None
# input_list = []
#
#
# while inp_data != "stop":
#    print("Введите число: ")
#    inp_data = input()
#    try:
#         if inp_data.isdigit():
#             input_list.append(int(inp_data))
#             print(f"Все хорошо. Добавлено число: {inp_data}")
#         elif inp_data == "stop":
#             print("Завершаем работу")
#         else:
#             raise MyError("Вы ввели не число")
#    except MyError as err:
#         print(err)
# print(input_list)

# Execize 4 - 6
# from abc import ABC, abstractmethod
#
# class Storage:
#     def __init__(self, capacity: int, free: int, equipments):
#         self.capacity = capacity
#         self.free = free
#         self.equipments = equipments
#
#     def inputEquipment(self, other):
#         if self.free == 0:
#             return "Склад заполнен"
#         else:
#             self.equipments.append(other)
#             self.free = self.free - 1
#
#     def giveEquipment(self):
#         if self.free == self.capacity:
#             return "Склад пуст"
#         else:
#             a = self.equipments.pop()
#             self.capacity = self.capacity + 1
#         return a
#
#     def items(self):
#         for x in range(len(self.equipments)):
#             print(self.equipments[x].properties_of_device())
#
# class Equipment(ABC):
#     def __init__(self, format):
#         self.format = format
#
#     @abstractmethod
#     def do_something(self):
#         pass
#
#     @abstractmethod
#     def properties_of_device(self):
#         print(f"{self.format}")
#
# class Printable(Equipment):
#     def __init__(self,  format, toner: bool):
#         super().__init__(format)
#         self.toner = toner
#
#     @abstractmethod
#     def do_something(self):
#         pass
#
#     def getToner(self):
#         self.toner = True
#
#     def setToner(self):
#         return self.toner
#
#     def have_toner(self):
#         if self.toner:
#             print("My toner is not empty")
#         else:
#             print("My toner is empty")
#
# class Printer(Printable):
#     name = "printer"
#     def __init__(self, format, toner):
#         super().__init__(format, toner)
#
#     def do_something(self):
#         print(f"I'm print {format}")
#
#     def properties_of_device(self):
#         print(f"{self.format} {self.toner}")
#
#
# class Scanner(Equipment):
#     name = "scanner"
#     def __init__(self, format):
#         super().__init__(format)
#
#     def do_something(self):
#         print(f"I'm scan {format}")
#
#     def properties_of_device(self):
#         print(f"{self.format}")
#
#
#
# class Xerox(Printable):
#     name = "xerox"
#     def __init__(self, format, toner):
#         super().__init__(format, toner)
#
#     def do_something(self):
#         print(f"I,m copy {format}")
#
#     def properties_of_device(self):
#         print(f"{self.format} {self.toner}")
#
# storage = Storage(1000, 1000, [])
# printer1 = Printer("A4", True)
# scanner = Scanner("A3")
# xerox = Xerox("A4", False)
# storage.inputEquipment(printer1)
# storage.inputEquipment(scanner)
# storage.inputEquipment(xerox)
# print(storage.items(), storage.free)

# Execize 7

class Complex_number:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex_number(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex_number(self.re * other.re - self.im * other.im,
                              self.im * other.re + self.re * other.im)
    def to_string(self):
        print(f"{self.re} + {self.im} i")

cn1 = Complex_number(1,2)
cn2 = Complex_number(3,4)
cn1.__add__(cn2).to_string()
cn1.__mul__(cn2).to_string()