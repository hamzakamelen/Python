# Control Flow (if else & loop)
# ------------------------------------------
# 1. Loops 

z=['H','A','M','Z','A']
for i in range(len(z)):
    print(z[i])

# 2. Take Number from user and write Table of user input to 10

table=int(input("Enter Table"))
for i in range(1,11):
    ans=i*table
    print(f"{table} x {i} = {ans}")

# 3. Basic Calculator 
x = int(input('Enter First Number'))
y = int(input('Enter Second Number'))
op = input("Enter Any Operation +,-,x,/")
print("\nAnswer is: ")
if(op=='+'):
    print(x+y)
elif(op=='-'):
    print(x-y)
elif(op=='x'):
    print(x*y)
elif(op=='/'):
    print(x/y)
else:
    print("Invalid Number")

# 4. Check student name in List & give answer user if exist or not
studentNames=['Hamza','Sami','Muzammil','Wajahat','Moiz']
userName=input()
if('Hamza' in studentNames):
    print('User exist in data')
else:
    print('User not exist in data')

# 5. ONE digit Secret Number Game
secretNum = 5
userNum = int(input('Guess Secret Number 0-9 '))
if(userNum == secretNum):
    print('Congrats! You Won')
else:
    print('Better Luck Next Time')

# 6.TWO digit Secret Number Game
a=55
secretNum = str(a)
firstNum = input('Enter First Number')
if(firstNum == secretNum[0]):
    print('You Guess Right! \nNow its time to Guess Second Number ')
    secondNum = input('Enter Second Number')
    if(secondNum ==secretNum[1]):
        print('You Guess it Right! You Won')
    else:
        print('Hard Luck! Try Again')
else:
    print('Hard Luck! Try Again')

# 7. Take Password From User if Incorrect then re-render
password = '5566HAMZA'
i= 1
while i==1:
    userPassword = input('Enter Password: ')
    if(userPassword == password):
        i=0
        print("\nCorrect Password")
    else:
        print('\nIncorrect Password! Enter Again')

# 8. Ask user Which Gamne want to play

def OneDigit():
    secretNum = 5
    userNum = int(input('Guess Secret Number 0-9 '))
    if(userNum == secretNum):
        print('Congrats! You Won')
    else:
        print('Better Luck Next Time')
        
def TwoDigit():
    a=55
    secretNum = str(a)
    firstNum = input('Enter First Number')
    if(firstNum == secretNum[0]):
        print('You Guess Right! \nNow its time to Guess Second Number ')
        secondNum = input('Enter Second Number')
        if(secondNum ==secretNum[1]):
            print('You Guess it Right! You Won')
        else:
            print('Hard Luck! Try Again')
    else:
        print('Hard Luck! Try Again')

num = int(input("Enter 1 for One Digit Game 2 for Two Digit Game"))
if(num==1):
    OneDigit()
elif (num==2):
    TwoDigit()
else:
    print('Error: Invalid Choice')

# 9. Basic Calculator With Functions
def basicCalculator(a,b,operation):
    print("\nAnswer is: ")
    if(op=='+'):
        print(x+y)
    elif(op=='-'):
        print(x-y)
    elif(op=='x'):
        print(x*y)
    elif(op=='/'):
        print(x/y)
    else:
        print("Invalid Number")   

x = int(input('Enter First Number'))
y = int(input('Enter Second Number'))
op = input("Enter Any Operation +,-,x,/")
basicCalculator(x,y,op)





