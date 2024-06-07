import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = x * 2

plt.xlabel('Valores de x')
plt.ylabel('Valores de x')

plt.plot(x,y, 'o:g', linewidth = 3, markersize=20)
plt.show()

