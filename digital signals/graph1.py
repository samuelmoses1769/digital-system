import numpy as np
import matplotlib.pyplot as plt

def unit_step(t):
  

  return np.where(t >= 0, 1, 0)

t = np.linspace(-10, 10, 100)
u = unit_step(t)

plt.plot(t, u)
plt.xlabel('Time')
plt.ylabel('Unit step function')
plt.title('Unit step function')
plt.show()