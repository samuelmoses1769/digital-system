import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols('z')
n = sp.symbols('n', integer=True)

def z_transform(f):
    return sp.summation(f * z**(-n), (n, 0, sp.oo))

def inverse_z_transform(F):
    return sp.inverse_z_transform(F, z, n)

f_a = sp.sin(n)
f_b = 2*z / (2*z - 1)
f_c = z*(-3) / (1 - z*(-1))
f_d = z / (z - sp.Rational(1, 4))
f_e = 2*z / (1 - 2*z**(-1)) + 4*z / (z - sp.Rational(1, 2))

n_values = np.arange(0, 10, 1)

# Calculate functions' values for plotting
f_a_values = np.sin(n_values)
f_b_values = 2 * n_values / (2 * n_values - 1)
f_c_values = np.where(n_values >= 3, 1, 0)
f_d_values = (1/4)**n_values
f_e_values = 2*(n_values + 1) + 4 * (1/2)*n_values

plt.figure(figsize=(12, 8))

# Plot original functions
plt.subplot(2, 1, 1)
plt.plot(n_values, f_a_values, label='sin(n)')
# plt.stem(n_values, f_b_values, label='a^n')
plt.stem(n_values, f_c_values, label='u(n-3)')
plt.stem(n_values, f_d_values, label='(1/4)^n * u[n]')
# plt.stem(n_values, f_e_values, label='2^(n+1) + 4(1/2)^n')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Original Functions')
plt.legend()

# Plot inverse Z-transforms
plt.subplot(2, 1, 2)
plt.plot(n_values, f_b_values, label='(2z) / (2z - 1)')
plt.plot(n_values, f_e_values, label='(2z) / (2z - 1) + 4z / (z - 1/2)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Inverse Z-transforms')
plt.legend()

plt.tight_layout()
plt.show()