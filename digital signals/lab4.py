import sympy as sp

# Define the symbolic variables for the Laplace transform and time
s, t = sp.symbols('s t')

# Define the functions
F_a = 1/s
F_b = 10/(s**2 + 25) - 4/(s - 3)
F_c = sp.exp(-3*s)*(2*s + 7)/(s**2 + 16)
F_d = (s**2 + 5*s - 3)/((s**2 + 16)*(s - 2))

# Define the inverse Laplace transform function
def inv_laplace_transform(F, t):
    return sp.inverse_laplace_transform(F, s, t)

# Calculate the inverse Laplace transforms
F_a_inv = inv_laplace_transform(F_a, t)
F_b_inv = inv_laplace_transform(F_b, t)
F_c_inv = inv_laplace_transform(F_c, t)
F_d_inv = inv_laplace_transform(F_d, t)

# Print the results
print("Inverse Laplace transform of F_a(s):", F_a_inv)
print("Inverse Laplace transform of F_b(s):", F_b_inv)
print("Inverse Laplace transform of F_c(s):", F_c_inv)
print("Inverse Laplace transform of F_d(s):", F_d_inv)

# Define the Laplace transform function
def laplace_transform(f, t):
    return sp.laplace_transform(f, t, s)

# Verify the results by applying the Laplace transform
F_a_laplace = laplace_transform(F_a_inv, t)
F_b_laplace = laplace_transform(F_b_inv, t)
F_c_laplace = laplace_transform(F_c_inv, t)
F_d_laplace = laplace_transform(F_d_inv, t)

# Print the verifications
print("Laplace transform of F_a^(-1)(t):", F_a_laplace)
print("Laplace transform of F_b^(-1)(t):", F_b_laplace)
print("Laplace transform of F_c^(-1)(t):", F_c_laplace)
print("Laplace transform of F_d^(-1)(t):", F_d_laplace)