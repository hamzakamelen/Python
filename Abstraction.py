
from abc import ABC,abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         pass
# class Triangle(Polygon):
#     def no_of_sides(self):
#         print('I have three sides')
# class Pentagon(Polygon):
#     def no_of_sides(self):
#         print('I have five sides')
# class Hexagon(Polygon):
#     def no_of_sides(self):
#         print('I have six sides')

# T = Triangle()
# T.no_of_sides()

# P = Pentagon()
# P.no_of_sides()

# H = Hexagon()
# H.no_of_sides()

class Employee(ABC):
    @abstractmethod
    def Name(self):
        pass

class Person1(Employee):
    def Name(self):
        print('Name is Hamza Kamelen')
class Person2(Employee):
    def Name(self):
        print('Name is Sami Mansoori')
class Person3(Employee):
    def Name(self):
        print('Name is Muzammil Mansoori')

H=Person1()
H.Name()
S = Person2()
S.Name()
W = Person3()
W.Name()