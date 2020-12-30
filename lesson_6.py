# Execize 1

import time


# class TrafficLight:
#     __color = ''
#
#     def running(self):
#         n = 0
#         while n < 2:
#             TrafficLight.__color = "red"
#             print(TrafficLight.__color)
#             time.sleep(3)
#             TrafficLight.__color = "yellow"
#             print(TrafficLight.__color)
#             time.sleep(2)
#             TrafficLight.__color = "green"
#             print(TrafficLight.__color)
#             time.sleep(10)
#             n += 1
#
# trafficlight = TrafficLight()
# trafficlight.running()

# Execize 2

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def square(self):
#         s = self._length * self._width
#         return s
# road = Road(5000, 5)
# mass = road.square() * 25 * 0.05
# print(mass)

# Execize 3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self.__wage = wage
#         self.__bonus = bonus
#         self.__income = {"wage": wage, "bonus": bonus}
#     def get_income(self):
#         return  self.__income
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage,bonus)
#     def get_full_name(self):
#         return f"{self.name} {self.surname}"
#     def get_total_income(self):
#         return self.get_income()["wage"] + self.get_income()["bonus"]
#
# pos = Position("Bob", "Jonson", "manager", 50000,10000)
#
#
# print(pos.name)
# print(pos.get_full_name(), pos.get_total_income())

# Execize 4
# class Car:
#     is_police = False
#
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#
#     def go(self):
#         print("Car start")
#
#     def show_speed(self):
#         print(f"Car is dirving with speed {self.speed}")
#
#     def stop(self):
#         print("Car sopped")
#
#     def turn(self, direction):
#         print(f"Car turn {direction}")
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name):
#         super().__init__(speed, color, name)
#
#     def show_speed(self):
#         if (self.speed <= 60):
#             print(f"Car is dirving with speed {self.speed}")
#         else:
#             print("Warning! You speed more than 60")
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name):
#         super().__init__(speed, color, name)
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name):
#         super().__init__(speed, color, name)
#
#     def show_speed(self):
#         if (self.speed <= 60):
#             print(f"Car is dirving with speed {self.speed}")
#         else:
#             print("Warning! You speed more than 40")
#
#
# class PoliceCar(Car):
#     is_police = True
#     def __init__(self, speed, color, name):
#         super().__init__(speed, color, name)
#
#
# police = PoliceCar(100, "black", "Ford")
# town = TownCar(50, "white", "Atos")
# print(police.is_police)
# print(town.is_police)
# police.turn("right")
# town.show_speed()


# Execize 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} write")

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} write by ink")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} write by lead")

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} write by toner")

pen = Pen("ballpoint")
pencil = Pencil("simple")
handle = Handle("black")
st =Stationery("something")
pen.draw()
pencil.draw()
handle.draw()
st.draw()
