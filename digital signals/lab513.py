import numpy as np
import matplotlib.pyplot as plt


def f(n):
    return np.heaviside(n - 3, 1)


def z_transform(f_n, n_values, z):
    F_z = np.sum([f_n(n) * z**(-n) for n in n_values])
    return F_z


n_values = np.arange(0, 10)


z_values = np.linspace(0, 2, 100)


f_values = [f(n) for n in n_values]


F_z_values = [z_transform(f, n_values, complex(0, z)) for z in z_values]


plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(n_values, f_values)
plt.title('Original Function f(n) = u(n-3)')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.grid(True)


plt.subplot(2, 1, 2)
plt.plot(z_values, np.abs(F_z_values))
plt.title('Magnitude of Z-transform of f(n) = u(n-3)')
plt.xlabel('Re(z)')
plt.ylabel('|F(z)|')
plt.grid(True)

plt.tight_layout()
plt.show()