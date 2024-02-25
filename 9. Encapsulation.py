# Encapsulation

# Public Access Modifier
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")

Sami_Mansoori = Employee("Sami",55)
Sami_Mansoori.display()
print(Sami_Mansoori.age)

# Private Access Modifier
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposit Successful,\n New Balance is {self.__balance}")
    def withDraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print(f"Withdrawl is successful \n Remaining Balance is {self.__balance}")
    def showbalance(self):
        print(f'Current Balance is {self.__balance}')

Account1 = BankAccount('SAMI',2000)
# print("Access Private method/member",Account1.__balance)
Account1.deposit(200)
Account1.withDraw(100)
Account1.showbalance()


# Protected Access Modifier
class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    def _display(self):
        print(f"Person Name: {self.name}")
        print(f"Person Age: {self._age}")

Wajahat_Mansoori = Person("Wajahat",55)
Wajahat_Mansoori._display()
print(Wajahat_Mansoori._age)
Wajahat_Mansoori._age = 10000
print(Wajahat_Mansoori._age)

# Protected Access Modifier
# class Person:
#     def __init__(self,name,age,id):
#         self.name = name
#         self.age = age
#         self._id = id
#     def display(self):
#         print(f"Name is {self.name}")
#         print(f"Age is {self.age}")
#         print(f"ID is {self._id}")
# class Student(Person)