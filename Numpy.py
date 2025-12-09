#NUMPY

# NumPy(Numerical Python) is a fundamental library for Python numerical computing. It provides efficient 
# multi-dimensional array objects and various mathematical functions for handling large datasets making it a 
# critical tool for professionals in fields that require heavy computation.

# Key Features of NumPy
# NumPy has various features that make it popular over lists.

# N-Dimensional Arrays: NumPy's core feature is ndarray, a N-dimensional array object that supports homogeneous 
# data types.
# Arrays with High Performance: Arrays are stored in contiguous memory locations, enabling faster computations 
# than Python lists (Please see Numpy Array vs Python List for details).
# Broadcasting: This allows element-wise computations between arrays of different shapes. It simplifies 
# operations on arrays of various shapes by automatically aligning their dimensions without creating new data.
# Vectorization: Eliminates the need for explicit Python loops by applying operations directly on entire arrays.
# Linear algebra: NumPy contains routines for linear algebra operations, such as matrix multiplication, 
# decompositions, and determinants.


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)

#Output: (2, 3)    #output is a tuple representing the dimensions of the array

print(arr.size)
#Output: 6    

print(arr.dtype)

#ndim gives the number of dimensions (axes) of the array.
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.ndim)
#Output: 2    #The array has 2 dimensions (rows and columns).

# itemsize gives the size in bytes of each element in the array.
# Possible Output: 8 That means each element (like 1, 2, 3) occupies 8 bytes (for int64).

# nbytes gives the total number of bytes consumed by the array.
# Output: 48    6 elements × 8 bytes = 48 bytes

# reshape vs shape
# shape : Tells you the current dimensions of the array.
# reshape : Creates a new view or new array with different dimensions (without changing the data).

arr2 = arr.reshape(3, 2)
print(arr2)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]


#Basic Indexing (1D array)
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

#Access elements
print(arr[0])   # 10
print(arr[2])   # 30
print(arr[-1])  # 50 (last element)

#Slicing (1D array)
arr[start : end : step]

print(arr[1:4])      # [20 30 40]
print(arr[:3])       # [10 20 30]
print(arr[2:])       # [30 40 50]
print(arr[::2])      # [10 30 50]
print(arr[::-1])     # reverse → [50 40 30 20 10]

#Indexing in 2D array (rows & columns)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

#Access one element
print(arr[0, 1])   # 2
print(arr[2, 2])   # 9
print(arr[1, -1])  # 6

#Row and Column slicing
#Whole row
print(arr[1])     # [4 5 6]

#Whole column
print(arr[:, 1])  # [2 5 8]

#Multiple rows
print(arr[0:2])
# [[1 2 3]
#  [4 5 6]]

#Multiple columns
print(arr[:, 0:2])
# [[1 2]
#  [4 5]
#  [7 8]]

#Slicing both rows AND columns
print(arr[0:2, 1:3])

# Output:
# [[2 3]
#  [5 6]]

#Using steps in 2D slicing
print(arr[::2, ::2])

# Output:
# [[1 3]
#  [7 9]]


#Boolean Indexing (important!)
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])

# Output:
# [30 40 50]


#Fancy Indexing (index using lists/arrays)
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 3, 4]])

# Output:
# [10 40 50]

# matrix = np.array([[1, 2], [3, 4], [5, 6]])
# print(matrix[[0, 2], [1, 0]])

# This picks:
# (0,1) → 2
# (2,0) → 5

# Output:
# [2 5]

#Modifying values using indexing/slicing
#Modify a single element
arr = np.array([1,2,3,4])
arr[2] = 99
print(arr)   # [1 2 99 4]

#Modify a slice (important: slice is a view, not a copy)
arr = np.array([1,2,3,4])
arr[1:3] = 100
print(arr)

# Output:
# [  1 100 100   4]

#Difference: Indexing vs Slicing
# Operation	Type	Returns
# arr[2]	Indexing	A single value
# arr[1:3]	Slicing	A view (changes original array)

a = np.array([1,2,3,4])
b = a[1:3]
b[:] = 9
print(a)

# Output:
# [1 9 9 4]

#Slicing does NOT create a new array, it shares memory with the original.


#Element-wise Arithmetic Operations
#NumPy operations are vectorized, meaning they apply to every element automatically.

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

#Addition
print(arr1 + arr2)

# Output:
# [5 7 9]

#Subtraction
print(arr2 - arr1)

# Output:
# [3 3 3]

#Multiplication
print(arr1 * arr2)

# Output:
# [ 4 10 18]

#Division
print(arr2 / arr1)


# Output:
# [4.  2.5 2. ]

# Exponent
print(arr1 ** 2)

# Output:
# [1 4 9]

# Modulus
print(arr2 % arr1)

# Output:
# [0 1 0]

#Mathematical Functions (Universal Functions / ufuncs)

#NumPy has many built-in math functions:
arr = np.array([1, 2, 3])

#Square root
np.sqrt(arr)  

#Exponential
np.exp(arr)

#Logarithm
np.log(arr)

#Sine, cosine, tangent
np.sin(arr)
np.cos(arr)
np.tan(arr)

#Absolute value
np.abs([-1, -5, 2])

#Array Comparisons (Boolean results)
arr = np.array([10, 20, 30, 40])

#Comparisons
print(arr > 25)

#Output:
#[False False  True  True]


#You can also compare arrays:
arr1 = np.array([1,2,3])
arr2 = np.array([3,2,1])
print(arr1 == arr2)

# Output:
# [False  True False]

#Aggregation Operations (sum, mean, etc.)
arr = np.array([1, 2, 3, 4])

#Sum
np.sum(arr)      # 10

#Mean
np.mean(arr)     # 2.5

#Min & Max
np.min(arr)      # 1
np.max(arr)      # 4

#Product
np.prod(arr)     # 24

#Standard deviation & variance
np.std(arr)      # 1.118...
np.var(arr)      # 1.25

#Index of min/max
np.argmin(arr)   # 0
np.argmax(arr)   # 3

#Aggregation along axes (2D arrays)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

#Sum of each column (axis=0)
np.sum(arr, axis=0)

# Output:
# [5 7 9]

#Sum of each row (axis=1)
np.sum(arr, axis=1)

# Output:
# [ 6 15]

#Broadcasting allows operations on arrays of different shapes.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr + 10)

# Output:
# [[11 12 13]
#  [14 15 16]]

#Scalar 10 is broadcast to all elements.

row = np.array([1, 2, 3])
print(arr + row)


# Output:
# [[2 4 6]
#  [5 7 9]]

#Dot Product & Matrix Multiplication
#Dot product (1D)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a, b))

#Output:
#32  # (1*4 + 2*5 + 3*6)

#Matrix multiplication (@ operator)
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])

print(A @ B)

# Output:
# [[19 22]
#  [43 50]]

#In-place operations
#These modify the array without creating a copy.

arr = np.array([1,2,3])
arr += 5
print(arr)

# Output:
# [6 7 8]

#np.arange()
#Creates an array with values in a range with a given step
#Similar to Python’s range() but returns a NumPy array.
np.arange(start, stop, step)

import numpy as np
arr = np.arange(1, 10, 2)
print(arr)

# Output:
# [1 3 5 7 9]

# Notes:
# stop is exclusive
# step can be a float
# Example with float:

np.arange(0, 1, 0.2)
# Output:
# [0.  0.2 0.4 0.6 0.8]

#np.linspace()
#Creates an array with evenly spaced numbers between two values.
#You specify how many points you want.

np.linspace(start, stop, num)

arr = np.linspace(0, 1, 5)
print(arr)

# Output:
# [0.   0.25 0.5  0.75 1.  ]

# Notes:
# Unlike arange, here stop is included
# Useful in graphs, scientific calculations

#np.zeros()
#Creates an array filled with 0s
np.zeros(shape)

# Example (1D):
# np.zeros(5)

# Output:
# [0. 0. 0. 0. 0.]


np.zeros((2, 3))

# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

#np.ones()
#Creates an array filled with 1s
np.ones(shape)


np.ones((3, 2))

# Output:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

#np.random (Generating Random Arrays)
#NumPy provides many functions to generate random data.

np.random.rand()

#Generates random float numbers between 0 and 1
np.random.rand(2, 3)

# Output:
# [[0.31 0.44 0.92]
#  [0.11 0.53 0.72]]

np.random.randn()
#Random numbers from standard normal distribution (mean = 0, std = 1)

np.random.randn(3)

np.random.randint()
#Random integers within a range

np.random.randint(low, high, size)

np.random.randint(1, 10, (2, 3))

# Output:
# [[7 3 1]
#  [9 2 4]]

# np.random.random()
# Random floats in range [0, 1)

np.random.random((2, 2))



# Vectorization means performing operations on entire NumPy arrays at once instead of using Python loops.
# NumPy uses optimized C code under the hood → making operations faster, cleaner, and more readable.

#Without Vectorization (Python loop)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = []
for i in arr:
    result.append(i * 2)

print(result)

#With Vectorization (NumPy)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
print(result)

# Vectorization With NumPy Universal Functions (ufuncs)
# NumPy provides many built-in vectorized functions:
# Function	Meaning
# np.sqrt(a)	Square root
# np.exp(a)	Exponential
# np.log(a)	Natural log
# np.sin(a)	Sine
# np.sum(a)	Sum
# np.mean(a)	Mean

#Real Power of Vectorization — Broadcasting
arr = np.array([1,2,3])
print(arr + 10)

# Output:
# [11 12 13]