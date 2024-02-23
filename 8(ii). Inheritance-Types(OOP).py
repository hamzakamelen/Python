# -----------------------------1. Simple Inheritance-----------------------------
class Fan:
    def __init__(self,name,company_name):
        self.OwnerName=name
        self.company_Name=company_name
    def ShowOwnerName(self):
        print(f'Owner Name == {self.OwnerName}')
    def ShowCompanyName(self):
        print(f'Company Name == {self.company_Name}')

class RoyalFan(Fan):
    def __init__(self,name,companyName,Color,Price):
        super().__init__(name,companyName)
        self.color = Color
        self.price = Price
    def ShowColor(self):
        print(f'Color of Royal Fan == {self.color}')
    def ShowPrice(self):
        print(f'Price of Royal Fan == {self.price}')
        
ownername= input('Enter Owner Name')
companyname= input('Enter company Name')
color=input('Enter Color')
price=int(input('Enter Price'))
Purchaser1 = RoyalFan(ownername,companyname,color,price)
Purchaser1.ShowOwnerName()
Purchaser1.ShowPrice()
# -----------------------------2. Multiple Inheritance-----------------------------
class Muzammil:
    def __init__(self):
        self.glasses = True
        self.Educated = True
        self.ShirtColor= 'Grey'
        self.AI_Student = True
class Moiz:
    def __init__(self):
        self.keyboard = True
        self.bike = True
        self.ResidentrialAddress = 'Saddar'
#         self.AI_Student = False
class Wajahat(Muzammil,Moiz):
    def __init__(self):
        super().__init__()
#         Moiz.__init__(self)
#         Muzammil.__init__(self)
        print(f'Glasses == {self.glasses}')
        print(f'Bike == {self.bike}')
        print(f'AI_Student == {self.AI_Student}')
        
Person1 = Wajahat()

# -----------------------------3. Multi Level Inheritance-----------------------------
class Computer:
    def __init__(self):
        self.OS = 'Windows'
        self.keyboard = True
        self.screen = True
        self.company = 'Dell'
class Laptop(Computer):
    def __init__(self):
        super().__init__()
        self.camera = True
        self.price  = 100000
class Mobile(Laptop):
    def __init__(self):
        super().__init__()
        self.OS = 'Android'
        print(f'{self.OS},{self.price}')
MB1 = Mobile()
# -----------------------------4. Hierarchy Inheritance-----------------------------
class ABCD_Plaza:
    cementUsed = 'ABCD Company'
    builders = 5000
    color = 'white'
    area = 'ABCD'
class SecondFloor(ABCD_Plaza):
    def __init__(self):
        self.persons=5
        self.rooms = 5
        self.ownerName = 'Sami'
class ThirdFloor(ABCD_Plaza):
    def __init__(self):
        self.persons=8
        self.rooms = 4
        self.ownerName = 'Muzammil'
        
Sami = SecondFloor()
print(Sami.rooms, Sami.cementUsed)

Muzammil = ThirdFloor()
print(Muzammil.rooms, Muzammil.cementUsed)
    
# -----------------------------5. Hybrid Inheritance-----------------------------
class Vehicle:
    def Company(self):
        self.Company = input('Enter Company of Vehicle')
        print(f'Company of Vehicle is === {self.Company}')
    def OwnerName(self):
        self.owner_Name = input('Enter owner_Name of Vehicle')
        print(f'owner_Name of Vehicle is === {self.owner_Name}')
        
class Bike(Vehicle):
    def Price(self):
        self.price= input('Enter Price of Vehicle')
        print(f'Price of Vehicle is === {self.price}')
    def Wheels(self):
        self.Wheels = input('Enter Wheels of Vehicle')
        print(f'Wheels of Vehicle is === {self.Wheels}')
class Car(Vehicle):
    def Km(self):
        self.Km= input('Enter Km of Vehicle Running')
        print(f'Km of Vehicle Running is === {self.Km}')
    def Country(self):
        self.Country = input('Enter Country of Vehicle')
        print(f'Country of Vehicle is === {self.Country}')
# -----------------Bike--------------
class Honda125(Bike):
    def SpeedHonda125(self):
        self.Speed = input('Enter Speed of Vehicle')
        print(f'Speed of Vehicle is === {self.Speed}')
    def ModelHonda125(self):
        self.Model = input('Enter ModelHonda125 of Vehicle')
        print(f'ModelHonda125 of Vehicle is === {self.Model}')   
class CG125(Bike):
    def SpeedCG125(self):
        self.Speed = input('Enter Speed of Vehicle')
        print(f'Speed of Vehicle is === {self.Speed}')
    def ModelCG125(self):
        self.Model = input('Enter Speed of Model')
        print(f'Model of Vehicle is === {self.Model}')
class Civic(Car):
    def SteeringColor(self):
        print('Steering Color is Red')
    def Tyres(self):
        print('MRF Tyres')

class Road(Honda125,Civic):
    def RoadName(self):
        self.RoadName = input('Enter Speed of RoadName')
        print(f'RoadName of Vehicle is === {self.RoadName}')
V1 = Road()
V1.RoadName()
V1.ModelHonda125()
V1.Wheels()
V1.OwnerName()
# ----------------
print('-----------------Next-----------------')
V1.Tyres()
V1.Km()
V1.OwnerName()
print('-----------------404 Error-----------------')
V1.SpeedCG125()