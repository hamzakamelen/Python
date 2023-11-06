# Python List 
# 1. Age of 5 Students
ageofStudents = [10,23,15,20,31,31]

# Access List
print(ageofStudents[3])

# Index from 2 to 4
print(ageofStudents[2:5])

# All List Elements
print(ageofStudents[:])

# Index from 3 to end
print(ageofStudents[3:])

# Add Elements at the end
ageofStudents.append(44)
print(ageofStudents)

# Combine two lists
ageofMaleStudents = [3,44,55,66,77]
ageofMaleStudents.extend(ageofStudents)
print(ageofMaleStudents)

# Add Element to Specific Index
ageofMaleStudents.insert(3,50)
print(ageofMaleStudents)

# Change Specific Item
ageofMaleStudents[3] = 222
print(ageofMaleStudents)

# Delete Item By Index
del ageofMaleStudents[2]
print(ageofMaleStudents)

# Remove Item By Value
ageofMaleStudents.remove(222)
print(ageofMaleStudents)

# Remove with Pop Method
ageofMaleStudents.pop(4)
print(ageofMaleStudents)

# Count Similar numbers
ageofStudents.count(31)

# Sorting Ascending
ageofMaleStudents.sort()
print(ageofMaleStudents)

# Sorting Descending
ageofMaleStudents.sort(reverse=True)
print(ageofMaleStudents)

# Check if Element Exist
print(3 in ageofMaleStudents)

# Length of List
len(ageofMaleStudents)

# Checking Type
print(type(ageofMaleStudents))


# Python Tuple
# 1. Create Tuple
lang = ('Python','Javascript','C','C++')
print(lang)

# Can Create Tuple without paranthesis
my_tuple = 1, 2, 3
print(my_tuple)

# Type
print(type(lang))

studentID = {1,2,9,8,5}
print(studentID)
# Type
print(type(studentID))

# Duplicate Elements
numbers={2,4,4,6,8,8}
print(numbers)

# Add Element
numbers.add(64)
print(numbers)

# Combine two Sets
studentID.update(numbers)
print(studentID)

# Delete Element from Sets
studentID.discard(5)
print(studentID)

# Maximum Value
print(max(studentID))

# Maximum Value
print(min(studentID))

# Sorted
print(sorted(studentID))

# Sum
print(sum(studentID))

# Union of Two Sets
A = {1, 3, 5}
B = {0, 2, 4}

print('Union using |:', A | B)
print('Union using union():', A.union(B)) 

#  Two Sets
C = {1, 3, 5}
D = {1, 2, 3}

print('intersection using |:', C & D)
print('intersction using intersection():', C.intersection(D)) 

# Difference of Two Sets
E = {1, 3, 5}
F = {1, 2, 3}

print('Difference using |:', E - F)
print('Difference using difference():', E.difference(F))

# Check if Subset (All Eleemnts in second set)
print(E.issubset(F))  

# Check if Disjoint (Not All Eleemnts in second set)
print( E.isdisjoint(F)) 


# Dictionary
studentData = {"name":"Hamza","id":1,"rollNo":'22F-BSAI-09'}
print(studentData)

# Get By Key
print(studentData["name"])


# Change Value By Key
studentData["name"]= "HK"
print(studentData)

# Length
print(len(studentData))

# Add new key + value
studentData['batch'] = '22F'

# Delete by Key
studentData['rollNo']
print(studentData)

# Check Key if exist
print("rollNo" not in studentData )
print("name" in studentData )

# Get Value of KEy
scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}

result = scores.get('Physics')


print(scores) 







