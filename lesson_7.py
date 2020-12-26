# Execize 1

# class Matrix:
#     def __init__(self, list_2d):
#         self.matrix = list_2d
#
#     def __str__(self):
#         return '\n'.join('\t'.join(map(str, row))
#                          for row in self.matrix)
#
#     def __getitem__(self, ind):
#         return self.matrix[ind]
#
#     def __add__(self, other):
#         other = Matrix(other)
#         result = []
#         numbers = []
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[0])):
#                 summa = other[i][j] + self.matrix[i][j]
#                 numbers.append(summa)
#                 if len(numbers) == len(self.matrix):
#                     result.append(numbers)
#                     numbers = []
#         return Matrix(result)
#
# list1 = [[1,2], [1, -1]]
# list2 = [[2,0], [-1, 3]]
# matrix1 = Matrix(list1)
# matrix2 = Matrix(list2)
# print(matrix1.__str__())
# matrix = matrix1+matrix2
# print(matrix)

# Execize 2
# from abc import abstractmethod
#
#
# class Dress():
#     def __init__(self, volume = 50, height = 1.8):
#         self.volume = volume
#         self.height = height
#
#     @abstractmethod
#     def tissue_v(self):
#         pass
#
#     @abstractmethod
#     def tissue_h(self):
#         pass
#
# class Coat(Dress):
#     def __init__(self, volume):
#         super().__init__(volume)
#     def tissue_v(self):
#         return (self.volume/6.5 + 0.5)
#
# class Suit(Dress):
#     def __init__(self, height):
#         super().__init__(height)
#     def tissue_h(self):
#         return (2 * self.height + 0.3)
#
# coat = Coat(44)
# suit = Suit(1.8)
# print(coat.tissue_v())
# print(suit.tissue_h())

# Execize 3

class Cell():
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            print("substruction not valid")

    def __mult__(self, other):
        return Cell(self.number * other.number)

    def __div__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, n):
        a = self.number // n
        b = self.number % n
        str = "*"
        for i in range(a):
            print(f"{str * n}")
        print(f"{str * b}")


cell1 = Cell(10)
cell2 = Cell(5)
cell1.make_order(3)