"""
Part 2 : Indexing and Selection

1. Basic Indexing and Selection 
-    Create a NumPy array [5, 10, 15, 20, 25, 30]. Select and print: 
-    The first element. 
-    The last three elements. 
-    The elements at index positions 1 to 4. 
"""
import numpy as np
import random
NPArray = [5, 10, 15, 20, 25, 30]
print(f"The Original Array :\n {NPArray}\n")
print(f"The First Element :\n {NPArray[0]}\n")
print(f"The Last Three Element :\n {NPArray[-3:]}\n")
print(f"The Element At Index 1 to 4 :\n {NPArray[1:5]}\n")

"""
2. Slicing and Views 
-    Create a 3x3 matrix from np.arange(1, 10).reshape(3, 3) and: 
-    Select the second row. 
-    Select the first two columns. 
-    Extract a sub-matrix of shape (2,2). 
"""
Matrix = np.arange(1,10).reshape(3,3)
print(f"The Original 3 X 3 Matrix : \n{Matrix}\n")
print(f"The Second Row Of The Matrix :\n {Matrix[1,]}\n")
print(f"Sub Matrix With Shap 2 X 2 :\n {Matrix[0:2,0:2].reshape(2,2)}\n ")

"""
3. Broadcasting 
-    Create a 3x3 matrix and add 10 to every element. 
-    Multiply the first column by 2.
"""
BC_Array = np.random.randint(1,20,(3,3))
print(f"The Original 3 X 3 Array :\n {BC_Array}\n")
print(f"The Array After Adding 10 to every Element : \n {BC_Array + 10}\n")
print(f"The Array After Multiply the first column by 2 : \n {(BC_Array[0:,0]* 2).reshape(3,1)}\n")

"""
4. Copying Arrays 
-    Create a NumPy array and demonstrate 
     the difference between shallow and deep copies.
"""
Np_ARR = np.arange(1,11)
print(f"The Original Array :\n {Np_ARR}\n") 

# Applying Shallow Copy ""
Shallow_Copy = Np_ARR[:]
Shallow_Copy [0] = 20
print(f"The Array After Shallow Copy Modification :\n {Np_ARR}\n") 

# Applying Deep Copy :
Np_ARR = np.arange(1,11) # Rest The Original 
Deep_Copy = np.copy(Np_ARR)
Deep_Copy[0]= 20
print(f"The Array After Deep Copy Modification :\n {Np_ARR}\n") 
print(f"The Deep Copy Array :\n {Deep_Copy}\n") 

"""
5. Fancy Indexing 
-    Given arr = np.arange(10, 101, 10),
     select elements at index [0, 3, 5].
"""
arr = np.arange(10, 101, 10)
Select = arr[[0,3,5]]
print(f"The Selected Array :\n{Select}\n")