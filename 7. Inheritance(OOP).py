# ===========PastPapers===========
'''
Apply inheritance concepts, write a class Polygon with a method that
takes number of sides as input and another method that displays it.
Create a subclass triangle, which calls input and display methods from 
the parent class and contains a method to calculate the area of triangle.
Create object for triangle and call methods to take input,
calculate area of a triangle and display the result. and show the output
'''
class Polygon:
    def __init__(self):
        self.abc = {} 
    def Input(self):
        self.numOfSides = int(input('Enter Number of Sides '))
        for i in range(1,self.numOfSides+1):
           self.abc[i] = float(input(f'Enter Length{i}: '))
    def Display(self):
        print(f'{self.numOfSides} Sides of Shape:\n ')
        for iter in range(1,self.numOfSides+1):
            print(f'{iter} Value: {self.abc[iter]}\n')
class Triangle(Polygon):
    def __init__(self):
        super().__init__()
        super().Input()
        super().Display()
    def AreaofTriangle(self):
        if self.numOfSides == 2:
            self.areaofTriangle = 0.5*self.abc[1] * self.abc[2] 
            print(f'Area of Triangle: {self.areaofTriangle}')
p = Triangle()
p.AreaofTriangle()

# -----------Error Solve---------------------
class A:
    def __init__(self,n='Adam'):
        self.name = n

class B(A):
    def __init__(self, roll):
        super().__init__()  #changing
        self.roll = roll

Hamza = B(23)
print(Hamza.name)

# ------------Instance Variable------------------
"""Instance variable Woh variable hota hai jo sab objects k lye unique ho 
yeh __init__ k andr define hota hai"""
class Student:
    def __init__(self,name,fathername,GPA):
        self.name = name
        self.fathername = fathername
        self.GPA = GPA
Hamza = Student('Hamza','Kamelen','Dangerous')
print(Hamza.name,Hamza.fathername,Hamza.GPA)

# ------------Class Variable------------------
"""Class variable Woh variable hota hai jo sab objects main accessible ho(also known as static variable),
 yeh defined hota hai outside constructor/any method of class
 Eg: Counter"""

class Login:
    TotalUsers = 0
    def __init__(self,name,money):
        Login.TotalUsers += 1
        self.name = name
        self.money = money
        print(f'Name: {self.name}\nMoney: {self.money}\nTotalUsers: {self.TotalUsers} ')
Login('Hamza',2000)
Login('talha',4000)
# ---------------------------------------
""" ----Solve Y^x using OOP. in this programming method 'Calculate' 
does the calculation and methos 'display' show the output. """
class Question:
    def __init__(self,base,exponent):
        self.y = base
        self.x = exponent
    def Calculate(self):
        self.calculation = self.y**self.x
    print('Calculation Done')
    def Display(self):
        self.result = f"Answer of {self.y}^{self.x} is {self.calculation}"
        print(self.result)

Ans1 = Question(2,2)
Ans1.Calculate()
Ans1.Display()

Ans2 = Question(3,2)
Ans2.Calculate()
Ans2.Display()

# -----------Find Errors---------------------
class Base:
    def __init__ (self, name):
        self.name= name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__ (self, name, age, address):
        Child.__init__ (self, name, age)
        self.address = address
    def getAddress(self):
        return self.address

g = GrandChild("Object1", 23, "Warwick") 
print(g.getName(), g.getAge(), g.getAddress())

# No Errors

# --------------Sum of First 10 Numbers --------------------
sum = 0
for i in range(1,10):
    num = int(input(f'Enter {i} Number: '))
    sum+=num
print(f'Sum of First 10 Numbers: {sum}')