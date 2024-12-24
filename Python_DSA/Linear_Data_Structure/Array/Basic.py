# Declaration of Array

# In Python, all types of lists are created same way
arr = []

# Initialization of Array

# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a, b, c)

# Using the list() Constructor

# From a tuple
a = list((1, 2, 3, 'apple', 4.5))  

print(a)

# Creating a List with Repeated Elements
arr = [0] * 5

# Accessing List Elements
a = [10, 20, 30, 40, 50]

# Access first element
print(a[0])    

# Access last element
print(a[-1])

# Adding Elements into List

# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)

# Updating Elements into List
a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25 

print(a)

# Removing Elements from List
a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)

# Iterating Over Lists
a = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in a:
    print(item)

# Nested Lists and Multidimensional Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])


# Length of a List
# Using len()
a = [1, 2, 3, 4, 5]
length = len(a)
print(length)

# Maximum in a List
# Using max()
a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)

# Using reduce() function from functools
from functools import reduce

a = [10, 24, 76, 23, 12]

# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)

print(largest)

# Positions of maximum element in list
# Method 1: Using max() + enumerate() + list comprehension
# initializing list 
test_list = [8, 4, 6, 8, 2, 8] 
 
# printing list 
print("The original list : " + str(test_list)) 
 
# Positions of maximum element in list 
# Using list comprehension + max() + enumerate() 
# initializing list 
test_list = [8, 4, 6, 8, 2, 8]

temp = max(test_list) 
res = [i for i, j in enumerate(test_list) if j == temp] 
 
# Printing result 
print("The Positions of maximum element : " + str(res)) 

# Method 2: Using numpy
import numpy as np
 
# initializing list
test_list = [8, 4, 6, 8, 2, 8]
 
# printing list
print("The original list : " + str(test_list))
 
res = np.argwhere(np.array(test_list) == max(test_list))
 
# Printing result
print("The Positions of maximum element : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

# Method 3: Using pandas
import pandas as pd
 
# initializing list 
test_list = [8, 4, 6, 8, 2, 8]
 
# printing list 
print("The original list : " + str(test_list))
 
# create a pandas series from the original list
series = pd.Series(test_list)
 
# find the maximum value in the series
max_val = series.max()
 
# find the positions of maximum element in series
res = series[series == max_val].index.tolist()
 
# Printing result
print("The Positions of maximum element : " + str(res))

# Swap Two Elements in a List
a = [10, 20, 30, 40, 50]

# Swapping elements at index 0 and 4
# using multiple assignment
a[0], a[4] = a[4], a[0]

print(a)

# Using a Temporary Variable
a = [10, 20, 30, 40, 50]

# Using a temporary variable
# to swap elements at index 2 and 4
temp = a[2]
a[2] = a[4]
a[4] = temp

print(a)

# Check if element exists in list
a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list
if 30 in a:
    print("Element exists in the list")
else:
    print("Element does not exist")

# Using any()
a = [10, 20, 30, 40, 50]

# Check if 30 exists using any() function
flag = any(x == 30 for x in a)

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")

# Using count()
a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list using count()
if a.count(30) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist")