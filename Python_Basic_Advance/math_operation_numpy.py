#Mathematical operation using numpy
import numpy as np
array1= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array1)

array2= np.arange(1,10).reshape(3,3)
print(array2)

print(array1+array2)

add= np.add(array1,array2)
print("add is:",add)

sub=np.subtract(array1,array2)
print("Sub is:",sub)

mult=np.multiply(array1,array2)
print("Multiply:",mult)

divide=np.divide(array1,array2)
print("Divide is:",divide)

#product of two matric is used using "np.dot()or @"
product = np.dot(array1,array2)
print("Product is:",product)

print("Product is:",array1 @ array2)

#to find maximum value in matrix we use "max()" function

print("Max value in array max is:",product.max())

#To find max value in row and column
max=product.max(axis=0)
print("Max value in prod", product.max(axis=1))
print("Max value in column in product matrix is:",max)

#To find the min value in row and column
min=add.min(axis=1)
print("The min value in add matrix",min)
print("The min value in column in add matrix is:",add.min(axis=0))

#To find out the index
print("The index of min value in row is:",min.argmin())
print("The index of max value in column is:", max.argmax())

min=add.min(axis=0)
print("The min value in column in add matrix is:",min)
print("The index of max value in column is:", max.argmin())

max=add.max(axis=1)
print("The max value column in add matrix is:",max)
print("The index of max value in column is:",np.argmax(max))

