import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

z, n, a = sp.symbols('z n a')

f_n = a**n

F_z = sp.summation(f_n * z**(-n), (n, 0, sp.oo))

a_value = 0.5
F_z_with_value = F_z.subs(a, a_value)

n_values = np.arange(0, 10)
f_n_values = [a_value**n_val for n_val in n_values]

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(n_values, f_n_values, basefmt="b")
plt.title('Original Signal $f(n) = a^n$')
plt.xlabel('n')
plt.ylabel('$f(n)$')

frequency_range = np.linspace(0, 2*np.pi, 1000)
F_values = [sp.Abs(F_z_with_value.subs(z, np.exp(1j * omega))) for omega in frequency_range]

plt.subplot(2, 1, 2)
plt.plot(frequency_range, F_values, label=f'Magnitude of $F(z)$ for $a = {a_value}$')
plt.title('Magnitude of Z-transform of $f(n) = a^n$')
plt.xlabel('Frequency (radians)')
plt.ylabel('$|F(z)|$')
plt.legend()

plt.tight_layout()
plt.show()