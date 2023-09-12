#array concatenation and split

import numpy as np
array1 = np.arange(1,17).reshape(4,4)
print(array1)
array2=np.arange(16,32).reshape(4,4)
print(array2)
print(np.concatenate((array1,array2)))

#row wise concatenation
print(np.concatenate((array1,array2),axis = 1))

#alternative for row wisse concatenation is "hstack"
print(np.hstack((array1,array2)))

#splitting the array
print("split array is:",np.split(array1,2,axis=0))
print('split the given array',np.split(array2,2))