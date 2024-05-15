import sympy as sp

# Define symbols
s, t, a = sp.symbols('s t a')

# Define functions
y_a = t ** 2
y_b = sp.exp(-a * t) + sp.exp(-3 * a * t)
y_c = sp.exp(2 * t) * sp.sin(2 * t)
y_d = sp.exp(3 * t) + sp.cos(6 * t) - sp.exp(-3 * t) * sp.cos(6 * t)
y_e = sp.Heaviside(t - 2) + 2 * sp.Heaviside(t - 3) - 2 * sp.Rational(1,2)

# Compute Laplace transforms
Y_a = sp.laplace_transform(y_a, t, s)
Y_b = sp.laplace_transform(y_b, t, s)
Y_c = sp.laplace_transform(y_c, t, s)
Y_d = sp.laplace_transform(y_d, t, s)
Y_e = sp.laplace_transform(y_e, t, s)

# Display Laplace transforms
print("Laplace transform of y = t^2:", Y_a[0])
print("Laplace transform of v = e^(-a*t) + e^(-3*a*t):", Y_b[0])
print("Laplace transform of y = e^(2*t) * sin(2*t):", Y_c[0])
print("Laplace transform of y = e^(3*t) + cos(6*t) - e^(-3*t) * cos(6*t):", Y_d[0])
print("Laplace transform of y = u(t - 2) + 2u(t - 3) - 2r(t - 2):", Y_e[0])

# Define inverse Laplace transform symbols
t_ = sp.symbols('t_', real=True)

# Compute inverse Laplace transforms
y_a_inv = sp.inverse_laplace_transform(Y_a[0], s, t_)
y_b_inv = sp.inverse_laplace_transform(Y_b[0], s, t_)
y_c_inv = sp.inverse_laplace_transform(Y_c[0], s, t_)
y_d_inv = sp.inverse_laplace_transform(Y_d[0], s, t_)
y_e_inv = sp.inverse_laplace_transform(Y_e[0], s, t_)

# Display inverse Laplace transforms
print("Inverse Laplace transform of Laplace transform of y = t^2:", y_a_inv)
print("Inverse Laplace transform of Laplace transform of v = e^(-a*t) + e^(-3*a*t):", y_b_inv)
print("Inverse Laplace transform of Laplace transform of y = e^(2*t) * sin(2*t):", y_c_inv)
print("Inverse Laplace transform of Laplace transform of y = e^(3*t) + cos(6*t) - e^(-3*t) * cos(6*t):", y_d_inv)
print("Inverse Laplace transform of Laplace transform of y = u(t - 2) + 2u(t - 3) - 2r(t - 2):", y_e_inv)