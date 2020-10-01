import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.0001*np.pi)

plt.plot(x, np.sin(x), label = 'Sin')
plt.plot(x, np.cos(x), label = 'Cos')
plt.plot(a, np.tan(a), label = "Tan", color = "red")
plt.ylim(-10,10)
plt.legend()

plt.show()

#for line4, it is not a curve, just a pattern of ten thousands of points. People can try 'np. linspace' to improve their words
