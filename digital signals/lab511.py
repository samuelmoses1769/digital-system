import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

k_values = np.arange(0, 10)
f_k = np.sin(k_values)

z, k = sp.symbols('z k')

F_z = sp.laplace_transform(sp.sin(k), k, z, noconds=True)

F_values = [F_z.subs(z, np.exp(1j * k_val)) for k_val in k_values]

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.stem(k_values, f_k, basefmt="b")
plt.title('Original Signal $f(k) = \sin(k)$')
plt.xlabel('k')
plt.ylabel('$f(k)$')

plt.subplot(2, 1, 2)
plt.stem(k_values, np.abs(F_values), basefmt="r")  
plt.title('Magnitude of Z-transform of $f(k) = \sin(k)$')
plt.xlabel('k')
plt.ylabel('$|F(z)|$')

plt.tight_layout()
plt.show()