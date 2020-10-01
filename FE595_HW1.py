import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.0001*np.pi)

plt.plot(x, np.sin(x), label = 'Sin')
plt.plot(x, np.cos(x), label = 'Cos')
plt.legend()

plt.show()