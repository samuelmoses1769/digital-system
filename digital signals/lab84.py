import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 1000)  
x_t = np.cos(4 * t) + np.cos(7 * t)
y_t = np.cos(4 * (t - 3)) + np.cos(7 * (t - 3))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x_t, label='Input x(t)')
plt.title('Input Signal x(t) = cos(4t) + cos(7t)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(t, y_t, label='Output y(t)', color='orange')
plt.title('Output Signal y(t) = x(t - 3)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()