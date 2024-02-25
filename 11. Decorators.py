# Pass Function as Argument
def add(x,y):
    return x+y

def calculate(func,x,y):
    return func(x,y)

cal = calculate(add,3,5)
print(cal)

# Return a Function as a Value
def outer(name):
    def inner():
        return f"Hello {name}"
    return inner

call = outer("Hamza")
print(call())

# Python Decorators
def Hamza(func):
    def inner():
        print("I am Decorator")
        func()
    return inner

def ordinary():
    print("I am Ordinary")

abc = Hamza(ordinary)
abc()

# @ Symbol With Decorator

def Hamza1(func):
    def inner():
        print("I am Decorator --- Real")
        func()
    return inner

@Hamza1
def ordinary():
    print("I am Ordinary --- Real")

ordinary()

# ------
def smartdivide(func):
    def inner(a,b):
        print(f"I'm dividing {a} & {b}")
        if(b==0):
            print("Can't Divide")
            return
        return func(a,b)
    return inner

@smartdivide
def divide(a,b):
    res = a/b
    print(res)

divide(2,3)
divide(2,0)

# Chaining Decorators in Python

def Abc(func):
    def inner(name):
        print(f"Hello Old")
        func(name)
    return inner

def ABC(func):
    def inner(name):
        print(f"Hello New")
        func(name)
    return inner

@Abc
@ABC
def StudentName(msg):
    print(msg)

StudentName("Hamzaaaaa")

# -----------------------
class decoratingClass:
    def __init__(self,func):
        self.func =func
    def __call__(self,a,b):
        print(f"{self.func.__name__} Function")
        result = self.func(self,a,b)
        print(f"Result of {self.func.__name__} is {result}")
    
class Decorate:
    @decoratingClass
    def add(self,a,b):
        return a + b
    @decoratingClass
    def subtract(self,a,b):
        return a - b
    
abc = Decorate()
abc.add(5,2)
abc.subtract(5,3)