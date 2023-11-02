print("Hello World")

x= 5
y=8
print(x+y)

print("5"+"8")

print("Muzammil "+"Khalid")

x = "Muzammil "
y = "Khalid"
print(x+y)

x= "23"
print(x*2)

x= "Muzammil "
print(x*2)

x= "Muzammil "
print("y"*2)

x= int(input("Enter First Number "))
y = int(input("Enter Second Number"))
opt = input("Select Option A. Subtraction  B. Addition C. Multiplication D. Division")
if(opt=="A"):    
    print(x-y)
elif(opt=="B"):
     print(x+y)
elif(opt=="C"):
    print(x*y)
elif(opt=="D"):
    print(x/y)

for i in range(1,100,100):
    print(i)
# start stop step

firstName = input("Enter Your First Name")
lastName = input("Enter Your Last Name")
fatherName = input("Enter Your Father Name")
rollNo = input("Enter Your Roll #")

# for i in range(0,3):
#     x[i] = input("Marks")
#     addition += x[i]

English=int(input("Enter Marks of English"))
Urdu=int(input("Enter Marks of Urdu"))
Maths=int(input("Enter Marks of Maths"))
addition = English + Urdu + Maths
print("Sum of",addition)
avg = (English + Urdu + Maths)/3
print("Avg",avg)



