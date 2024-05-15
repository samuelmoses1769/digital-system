import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def system(y, t):
    y1, y2 = y
    dydt = [y2, y2 - 2*y1 + 1]
    return dydt
t = np.linspace(0, 10, 100)
y0 = [0, 0]
sol = odeint(system, y0, t)
impulse_response = sol[:, 0]
plt.figure()
plt.plot(t, impulse_response)
plt.title('Impulse Response')
plt.xlabel('Time')
plt.ylabel('Response')
plt.grid(True)
plt.show()
roots = np.roots([1, -1, -2])
print("The system is LTI.")
if all(root.real < 0 for root in roots):
    print("System is stable.")
else:
    print("System is unstable.")