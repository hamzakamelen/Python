# ==========Classes===============
# class Pen:
#     def __init__(self,Color,Diameter,Price):
#         self.Color = Color
#         print(Color)
#         self.Diameter = Diameter
#         print(Diameter)
#         self.Price = Price
#         print(Price)

# P1 = Pen("Red",20.5,500)

# class Class:
#     def __init__(self,Students,PositionHolders):
#         self.Students = Students
#         self.PositionHolders = PositionHolders
#         print(self.Students)
#     def ForeignStudents(self):
#             self.NewStu = self.PositionHolders - 5
#             print(self.NewStu)

# C1 = Class(50,20)
# C1.ForeignStudents()


# class Marksheet:
#     def __init__(self):
#         self.English = int(input("Enter English Marks "))
#         self.Urdu = int(input("Enter Urdu Marks "))
#         self.Math = int(input("Enter Math Marks "))
#         self.Computer = int(input("Enter Computer Marks "))
#     def Marksheet(self):
#         print('==========================================MarkSheet==========================================')
#         print(f"English: {self.English} \nUrdu: {self.Urdu} \nMath: {self.Math} \nComputer: {self.Computer}")
#         self.TotalMarks = self.English + self.Math + self.Urdu + self.Computer
#         print(f'Total Marks: {self.TotalMarks}')
#         self.Percentage = (self.TotalMarks*100)/400
#         print(f'Percentage: {self.Percentage}')
        

# Muzammil = Marksheet()
# Muzammil.Marksheet()

# class Marksheet:
#     def __init__(self):
#         self.totalMarks = 0 
#         for x in range(1,6):
#             self.Sub = int(input(f'Enter Marks of Sub {x} '))
#             self.totalMarks += self.Sub
        
#         print(self.totalMarks)
#         self.percentage = (self.totalMarks*100)/x*100
#         print(self.percentage)
#         print('pass') if self.percentage>=50 else print('Fail')


# Hamza = Marksheet()

# ============= Inheritance ===================
# class A:
#     def __init__(self):
#         self.name = 'Hamza Kamelen'
#     def CompSci(self):
#         self.CompSci = 50
#     def English(self):
#         self.English = 60
#     def OOP(self):
#         self.OOP = 70
# class B(A):
#     def __init__(self):
#         pass
#     def Maths(self):
#         self.Maths = 50
#     def Urdu(self):
#         self.Urdu = 60
#     def Science(self):
#         self.Science = 70
# H = B()
# H.English()
# ----------------------------
# class Vehicle:
#     def __init__(self):
#         self.color = 'black'
#         self.seats = '4'
#         self.weight = '50kg'
#     def EngineSpec(self):
#         self.number = 20
#         self.avg = '5ltr'

# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.ownername = 'Hamza'
#         print(f'{self.seats}')
#     def EngineSpec(self):
#         super().EngineSpec()  # Call the parent class's EngineSpec() method
#         self.life = '2years'
#     def ShowOutput(self):
#         print(f'Number: {self.number}\nAverage: {self.avg}\ncolor = {self.color}  ')

# HamzaBike = Bike()
# HamzaBike.EngineSpec() 
# HamzaBike.ShowOutput()
# print(HamzaBike.number)
# ----------------------------

# class Vehicle:
#     def __init__(self):
#         self.color = 'black'
#         self.seats = '4'
#         self.weight = '50kg'
#     def EngineSpec(self):
#         self.CC = 150
#         self.avg = '5ltr'

# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.ownername = 'Hamza'
#         print(f'The vehical is {self.seats} seated')
#     def details(self):
#         super().EngineSpec()  # Call the parent class's EngineSpec() method
#         self.life = '2years'
#     def ShowOutput(self):
#         print(f'Power of engine is : {self.CC}\nAverage: {self.avg}\ncolor : {self.color}  ')

# HamzaBike = Bike()
# HamzaBike.details() 
# HamzaBike.ShowOutput()

# ========= Nested Class =========

# class Student:
#     def __init__(self):
#         self.name = 'Hamza Kamelen'
#         self.language = 'Urdu'
#         self.fvtcolor = 'black'
#         print('Chal gai 1')

#     class Contact:
#         def __init__(self): 
#             self.email = 'hamza@gmail.com'
#             self.cellNo = '03112474407'
#             print('Chal gai 2')

# Hamza = Student()
# ContactUs = Hamza.Contact()
        #   OR
# Hamza = Student().Contact()

# -------------------------------------

