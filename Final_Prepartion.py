#1. Vehicle: Create a base class Vehicle with attributes like make, model, and year. Create subclasses for specific vehicle types like Car, Truck, and Motorcycle, inheriting from Vehicle and adding specific attributes and methods.
class Vehicle:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
  def start(self):
    print("Starting")
  def end(self):
    print("Ending")
     
class Car(Vehicle):
  def __init__(self,make,model,year,seats):
    super().__init__(make,model,year)
    self.seats = seats
  def Accelerate(self):
    print("Running")
     
class Truck(Vehicle):
  def __init__(self,make,model,year,load):
    super().__init__(make,model,year)
    self.load = load
  def Weight(self):
    print("2000 kg")
     
class Motorcycle(Vehicle):
  def __init__(self,make,model,year,persons):
    super().__init__(make,model,year)
    self.persons = persons
  def Licence_Available(self):
    print("Yes Available")
     
car = Car("Civic","12A",2023,4)
truck = Truck("Mazda","2018",2002,"80 kg")
bike = Motorcycle("Unique","2020",2023,2)

print("--------Car-------------")
car.start()
car.Accelerate()
print(car.seats,car.model,car.make)
car.end()
print("--------Truck-------------")
truck.start()
truck.Weight()
print(truck.load,truck.model,truck.make)
truck.end()
print("--------Motorcycle-------------")
bike.start()
bike.Licence_Available()
print(bike.persons,bike.model,bike.make)
bike.end()

# Shape: Design a base class Shape with methods for calculating area and perimeter. Create subclasses for specific shapes like Circle, Square, and Triangle, inheriting from Shape and implementing their own area and perimeter calculations.
# Shape      Area             Perimeter
# Circle A = π × r2     Circumference = 2πr
# Triangle A = ½ × b × h     S = perp+base+hyp
# Square A = a2           P = 4a
# Rectangle A = l × w       P = 2(l + w)
class Shape:
    def calculateArea(self):
        print("First, We Calculate Area")
    def calculatePerimeter(self):
        print("Now, We Calculate Perimeter")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculateArea(self):
        super().calculateArea()
        self.area = 3.142 * self.radius**2
        print(f"Area is {self.area}")
    def calculatePerimeter(self):
        super().calculatePerimeter()
        self.perimeter =2 * 3.142 * self.radius
        print(f"Perimeter is {self.perimeter}")
       
class Square(Shape):
        def __init__(self,side):
            self.side = side
        def calculateArea(self):
            super().calculateArea()
            self.area = self.side**2
            print(f"Area is {self.area}")
        def calculatePerimeter(self):
            super().calculatePerimeter()
            self.perimeter = 4 * self.side
            print(f"Perimeter is {self.perimeter}")

class Triangle(Shape):
        def __init__(self,perp,base,hyp):
            self.perp = perp
            self.base = base
            self.hyp = hyp
        def calculateArea(self):
            super().calculateArea()
            self.area = 1/2 * self.base * self.hyp
            print(f"Area is {self.area}")
        def calculatePerimeter(self):
            super().calculatePerimeter()
            self.perimeter = self.perp + self.base + self.hyp
            print(f"Perimeter is {self.perimeter}")
       
class Rectangle(Shape):
        def __init__(self,length,width):
            self.length = length
            self.width = width
        def calculateArea(self):
            super().calculateArea()
            self.area = self.length * self.width
            print(f"Area is {self.area}")
        def calculatePerimeter(self):
            super().calculatePerimeter()
            self.perimeter = 2(self.length + self.width)
            print(f"Perimeter is {self.perimeter}")



circle = Circle(20)
rectangle = Rectangle(10,5)
square = Square(20)
triangle = Triangle(10,20,30)

print("----------Circle--------------")
circle.calculateArea()
circle.calculatePerimeter()

print("----------Triangle--------------")
triangle.calculateArea()
triangle.calculatePerimeter()

print("----------Square--------------")
square.calculateArea()
square.calculatePerimeter()

print("----------Rectangle--------------")
rectangle.calculateArea()
rectangle.calculatePerimeter()


# Animal: Create a base class Animal with a method make_sound(). Create subclasses for specific animals like Dog, Cat, and Bird, inheriting from Animal and overriding make_sound() with their unique sounds.

class Animal:
    def make_sound(self):
        pass
   
class Dog(Animal):
    def make_sound(self):
        print("ABC")
       
class Cat(Animal):
    def make_sound(self):
        print("DEF")

class Bird(Animal):
    def make_sound(self):
        print("GHI")

dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()

# Employee: Design a base class Employee with methods for calculating salary. Create subclasses for specific employee types like Manager, Developer, and Salesperson, inheriting from Employee and implementing their own salary calculation logic.

class Employee:
    def __init__(self,name,Position,salary):
        self.name = name
        self.Position = Position
        self.salary =salary
    def CalculateSalary(self):
        pass

class Manager(Employee):
    def __init__(self,name,Position,salary,bonus):
        super().__init__(name,Position,salary)
        self.bonus = bonus
    def CalculateSalary(self):
        print(f"Salary of {self.Position} is {self.salary + self.bonus}")
       
class Developer(Employee):
    def __init__(self,name,Position,salary,extraHoursWorked):
        super().__init__(name,Position,salary)
        self.extraHoursWorked = extraHoursWorked
    def CalculateSalary(self):
        print(f"Salary of {self.Position} is {self.salary + (550 * self.extraHoursWorked) }")

class Salesman(Employee):
    def __init__(self,name,Position,salary,extraSales):
        super().__init__(name,Position,salary)
        self.extraSales = extraSales
    def CalculateSalary(self):
        print(f"Salary of {self.Position} is {self.salary + (55 * self.extraSales)}")
       
manager = Manager("Hamza","Manager",200000,30000)
developer = Developer("Wajahat","Developer",300000,50)
salesman = Salesman("Moiz","Salesman",100000,61)

manager.CalculateSalary()
developer.CalculateSalary()
salesman.CalculateSalary()
