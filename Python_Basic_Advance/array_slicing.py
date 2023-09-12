#Python numpy array slicing
import numpy as np
array = np.arange(1,101).reshape(10,10)
print(array)

print(array[0,0])
print(array[1])

#Slicing the array
print("This array gives desired column",array[:,0:1])

print("This array gives desired row and column:",array[2:6,3:7])