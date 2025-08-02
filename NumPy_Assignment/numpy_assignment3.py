"""
Part 3: NumPy Operations

1. Mathematical Functions 
-  Find the maximum, minimum, index of max, and index of min for the array 
    [3, 7, 2, 9, 12, 5, 10]. 
"""
import numpy as np
Arrr = np.array([3,7,2,9,12,5,10])
print(f"The Maximum number of The Array : \n {np.max(Arrr)} At Index {np.argmax(Arrr)}\n")
print(f"The Minimum number of The Array : \n {np.min(Arrr)} At Index {np.argmin(Arrr)}\n")

"""
2. Universal Array Functions 
-  1. Given arr = np.array([1, 2, 3, 4, 5]), apply the following functions: 
      a. Square root (sqrt()) 
      b. Exponential (exp()) 
      c. Sine (sin()) 
      d. Logarithm (log()) 
"""
aarr = np.array([1, 2, 3, 4, 5])
print(f"The Original Array : \n{aarr}\n" )
print(f"The Square Root Of The Array :\n{np.sqrt(aarr)}\n")
print(f"The Exponential Of The Array \n {np.exp(aarr)}\n")
print(f"The Sine Of The Array : \n {np.sin(aarr)}\n")
print(f"The Logarithm Of The Array : \n {np.log(aarr)}\n")