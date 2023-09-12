import numpy as np
array = np.arange(1,11).reshape(2,5)
print(array)

max= array.max(axis=0)
print("The maximum is:",max)
print("The index of max element is :",max.argmax())
print("The max value in entire array is ",array.max())
print("The index of max value in entire array is ",array.argmax())