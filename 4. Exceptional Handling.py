# Exceptional Handling

# ----------1----------- 
try:
    a=25
    b=0
    print(a/b)
except:
    print("Syntax Error")

# ---------- 2 ----------- 

try:
    a=int(input("Enter First Number"))
    b=int(input("Enter Second Number"))
    result=a/b
except TypeError:
    print('Number Data type Required')
except ValueError:
    print('Invalid Input')
except ZeroDivisionError:
    print('Incorrect Input')
except NameError:
    print('Invalid Syntax')
else:
    print('The result is' , result)
#Koi Exceptional nahi hogi to yeh chlega
finally:
    print("Thank Your for Using Python") 
#Koi Exceptional ho ya na ho yeh lazmi chlega

# -------------- Generate own Errors --------------------
x= input("Enter Your Name")
if not x.isalpha(): #isalpha means check krega kya input alphabet hai?
    raise ValueError('Enter String Text') #Raise Krega Error

studentName=input('Enter Your Name')
# fatherName = input('Enter Your father Name')

if studentName.isdigit():
    raise ValueError('Enter Correct Name')
