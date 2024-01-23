# --------------------- OPEN ENDED LAB ------------------------------- 
# Question: Create a class named as along with member function. Calculate pressure and volume. create class for two different shapes of pipes 
# and measure the pressure and volume of crosssection.
# Area  = pie x r2 , Volume  = Pie x r2 x l
# Area = lxb, Volume = l x b x h


class Parameter:
    def CalculatePressure(self,area,force):
        self.pressure = force/area
        print(f'\nPressure is {self.pressure}')
    def CalculateVolume(self,area, length):
        self.volume = area * length
        print(f'Volume is {self.volume}\n')

class Cylinder(Parameter):
    def __init__(self,radius,force,length):
        self.area = (3.142 * (radius*radius))
        self.force = force
        self.length = length

class Rectangle(Parameter):
    def __init__(self,force,length,breath,height):
        self.area = length*breath*height
        self.force = force
        self.length = length


P1 = Cylinder(20,10,30)
P2 = Rectangle(10,20,15,15)
P1.CalculatePressure(P1.area,P1.force)
P1.CalculateVolume(P1.area,P1.length)

P2.CalculatePressure(P2.area,P2.force)
P2.CalculateVolume(P2.area,P2.length)


















# class Parameter:
#     def CalculatePressure(Force,Area):
#         Pressure = Force/Area
#         print(Pressure)
#     def CalculateVolume(Area):
#         self.volume = self.area
#         print(self.volume)

# class Pipe1(Parameter):
#     def __init__(self):
#         self.force = 50
#         self.area = 40

# class Pipe2(Parameter):
#     def __init__(self):
#         self.force = 20
#         self.area = 30
    
# P1 = Pipe1().CalculatePressure
# P1 = Pipe1().CalculateVolume
