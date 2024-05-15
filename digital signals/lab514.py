import numpy as np
import matplotlib.pyplot as plt

def original_function(n):
    return (1/4)**n * (n >= 0)  # Original function: (1/4)^n * u(n)

def transformed_function(n):
    return (1/4)**n * (n >= 0)  # Transformed function: (1/4)^n * u(n)

n_values = np.arange(-10, 10, 1)  # Define the range of values for n

original_values = original_function(n_values)
transformed_values = transformed_function(n_values)

# Plotting original function separately
plt.figure(figsize=(8, 4))
plt.plot(n_values, original_values, label='Original Function: (1/4)^n * u(n)')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Original Function: (1/4)^n * u(n)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting both original and transformed functions together
plt.figure(figsize=(8, 4))
plt.plot(n_values, original_values, label='Original Function: (1/4)^n * u(n)')
plt.plot(n_values, transformed_values, label='Transformed Function: (1/4)^n * u(n)')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Plot of Original and Transformed Functions')
plt.legend()
plt.grid(True)
plt.show()