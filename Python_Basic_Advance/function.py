#There are two types of function
#They are "User-Defined" and "system-defined"

import numpy as np

#System-defined function
array = np.arange(2,10)
print(array)
function = np.mean(array)
print("The mean:",function)
function1 = np.median(array)
print("The median:", function1)

#user-defined function has two  part they are
#function defination and calling function
x=10
def add(x):
    return(x**2)
print("The square of", x, "is", add(x))

#creating a dividefunction
a=20
b=5
def divide(a,b):
    return(a/b)
print(a,"/",b,":",divide(a,b))


