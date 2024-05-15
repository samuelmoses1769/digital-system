import sympy as sp
import matplotlib.pyplot as plt

# Define symbols and functions
t = sp.symbols('t')
u = sp.Heaviside(t)

# Define functions
f = u * u.subs(t, 3 - t)
g = u - u.subs(t, t - 3)

# Create lists to store points
t_values = []
f_values = []
g_values = []

# Evaluate functions for different values of t
for i in range(-5, 6):
    t_val = i
    t_values.append(t_val)
    f_values.append(f.subs(t, t_val))
    g_values.append(g.subs(t, t_val))

# Plot the points
plt.plot(t_values, f_values, 'ro', label='f(t)')
plt.plot(t_values, g_values, 'bo', label='g(t)')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Plot of f(t) and g(t)')
plt.legend()
plt.grid(True)
plt.show()

# Compare expressions
if sp.simplify(f - g) == 0:
    print("The functions f(t) and g(t) are identical.")
else:
    print("The functions f(t) and g(t) are not identical.")

# Compute Laplace transforms
F = sp.laplace_transform(f, t, sp.symbols('s'))
G = sp.laplace_transform(g, t, sp.symbols('s'))

# Print Laplace transforms
print("L(f(t)) =", sp.simplify(F[0]))
print("L(g(t)) =", sp.simplify(G[0]))

# Compare Laplace transforms
if sp.simplify(F[0] - G[0]) == 0:
    print("L(f(t)) = L(g(t))")
else:
    print("L(f(t)) ≠ L(g(t))")