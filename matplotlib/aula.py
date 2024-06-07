import matplotlib.pyplot as plt
import numpy as np

# Grafico Plot
x = np.array([1,2,3,4])
y = x * 2

plt.xlabel('Valores de x')
plt.ylabel('Valores de x')
plt.plot(x,y, 'o:g', linewidth = 3, markersize=20)
plt.show()

# Plots multiplos
x = np.array([1,2,3,4])
y = x * 2
y2 = x*x
plt.xlabel('Valores de x')
plt.ylabel('Valores de x')
plt.plot(x,y, 'r-', x, y2 , 'b-')
plt.show()

# Plots multiplos de forma separada
x = np.array([1,2,3,4])
y = x * 2
y2 = x*x
plt.subplot(1, 2, 1)
plt.title('Linear')
plt.plot(x,y, 'r-')
plt.subplot(1, 2, 2)
plt.title('Exponencial')
plt.plot(x, y2 , 'b-')
plt.show()

