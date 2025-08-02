"""
Part 1: Creating NumPy Arrays

### Using Built-in Methods

Create the following arrays using NumPy built-in functions:

"""
import numpy as np 
#   An array of Numbers from 0 to 20 with a step of 2.

Array = np.arange(0,21,2)
print(f"\nArray Of Numbers From 0 To 20 With a Step Of 2 :\n {Array}\n")

#   A 3x3 identity matrix.

Iden_Matrix = np.identity(3)
print(f"A 3x3 Identity Matrix :\n {Iden_Matrix}\n") 

#  A 4x4 array filled with ones.

Ones_Array = np.ones((4,4))
print(f"A 4x4 Array Filled With Ones :\n {Ones_Array}\n") 

#  An array of 10 Equally Spaced Numbers between 5 and 50.

ES_Array = np.linspace(5,50,10)
print(f"An Array Of 10 Equally Spaced Numbers Between 5 And 50 :\n {ES_Array}\n") 



### 2. Creating Arrays from Lists


#  Convert a Python list `[10, 20, 30, 40, 50]` into a NumPy array.
Normal_List = [10,20,30,40,50]
Numpy_List = np.array(Normal_List)
print(f"The List Converted To NumPy :\n {Numpy_List}\n")



#  Generate a 3x3 matrix of random Numbers using:

#    - `np.random.rand()`

Rand_Matrix = np.random.rand(3,3)
print(f"3X3 rand Matrix (Uniform Distribution [0 , 1) ) :\n {Rand_Matrix}\n")
#    - `np.random.randn()`

Randn_Matrix = np.random.randn(3,3) 
print(f"3X3 rand-N Matrix (Normal (Gaussian) Distribution) :\n {Randn_Matrix}\n") 

#    - `np.random.randint()`

RandINT_Matrix = np.random.randint(0,100,size=(3,3)) # Start , Stop , (Size OF The Matrix)
print(f"3X3 rand-Int Matrix (Integers) :\n {RandINT_Matrix}\n") 

### 3. Array Attributes

# Print the **shape**, **size**, and **data type** of an array you created in the previous steps.
# Let's Test (ES_Array)
print(f"The Shape of The Array ( Equally Spaced Numbers Array ) : {ES_Array.shape}")
print(f"The Size of The Array ( Equally Spaced Numbers Array ) : {ES_Array.size}")
print(f"The Data Type of The Array ( Equally Spaced Numbers Array ) : {ES_Array.dtype}")