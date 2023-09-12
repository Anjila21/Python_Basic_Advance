#Numpy functions

import numpy as np

#arange()
include=np.arange(1,50,4)
print(include)

#linspace()
space = np.linspace(1,2,5)
print(space)

#reshape(): converts array into multidimensional array
array1= np.array([1,2,3,4,5,6])
reshape = array1.reshape(2,3)
print(reshape)

array2 = np.array([[1,2,2,2,3,1],[4,5,6,7,8,4]])
reshape2 = array2.reshape(4,3)
print(reshape2)

#ravel() and flatten(): converts multi-dimension array into 1D array
print(array2.ravel())
print(array2.flatten())

#transpose() : exchanges the rows and column of the inital matraix
print(reshape2.transpose())

example = np.arange(20,30).reshape(2,5)
print(example)