# ===========Operator Precedence===============

# 1.--------------Paranthesis-----------
paranthesis = (5+5+9+8+21)*(2+5+8+35)
print(paranthesis)
withoutParanthesis = 5+5+9+8+21*2+5+8+35
print(withoutParanthesis)
# Ans == paranthesis NotEqualto withoutParanthesis

# 2. --------------Exponential--------------
print(2**5)

# 3. --------------Negation--------------
x=5
print(-x)

# 4. --------------Divsion & Multiplication & Modulus--------------
print(25*5/5)

# 5. --------------Addition & Subtraction--------------
print(5-5+25)

# 6. --------------Bitwise--------------
a=5
b=7
# bin() convert to binary
c=bin(12)
print(c)
# d=bin(b)
# print('A is',a,'\nB is',b,'\nC is',c,'\nD is',d)
print(bin(a>>b))
print(bin(a<<b))



# 7. --------------Comparision--------------
x=8
print(x==5)
print(x>5)
print(x<5)
print(x>=8)
print(x<=9)
print(x!=5)

# 8. --------------Logical NOT, AND, OR--------------
A=True
B=False
print(~A , ~B)

print(A or B)
print(A | B)

print(A and B) 
print(A & B)


