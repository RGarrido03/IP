# Try running this program.
# Then change it to generate another subplot with the product of y1 and y2.

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

t = np.arange(0.0, 5.0, 0.1)  # try printing t
plt.subplot(3, 1, 1)
y1 = np.exp(-t)
plt.plot(t, y1, 'b')  # try 'g' or 'bo' or 'k+'

plt.subplot(3, 1, 2)
y2 = np.cos(2*np.pi*t)
y3 = y1 * y2
plt.plot(t, y2, 'ro-', t, y3, "g")

plt.subplot(3, 1, 3)
t = np.arange(-3,2,0.1)
y4 = t**2 + 3*t + 1
plt.grid()
plt.plot(t, y4, "r")

plt.show()

