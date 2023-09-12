#random sampling with python
import numpy as np
import random

print(np.random.random(1))

print(np.random.random((3,3)))

print(np.random.randint(1,4))

print(np.random.randint(1,4,(4,4)))

print(np.random.rand(3))

print(np.random.randn(3,3))

x=[10,2,30,35,45,60,55]
print(np.random.permutation(x))