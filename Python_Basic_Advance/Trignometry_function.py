#Trignomtery in numpy
import numpy as np
import matplotlib.pyplot as plt
print(np.sin(180))
x_sin = np.arange(0,3*np.pi,0.1)
print(x_sin)

y_sin=np.sin(x_sin)
plt.plot(x_sin,y_sin)
plt.show()
y_tan=np.tan(x_sin)
plt.plot(x_sin,y_tan)
plt.show()