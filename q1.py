import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for 'a' (adjust as needed)
a_values = np.linspace(-2, 2, 1000)  # Creates 1000 points from -2 to 2

# Define the stability check function
def check_stability(a):
    return abs(a) < 1  # True for stable, False for unstable

# Calculate stability results for each 'a' value
stable_results = np.vectorize(check_stability)(a_values)

# Create the plot
plt.figure(figsize=(8, 6))  # Adjust figure size as desired
plt.axhline(y=1, color='red', linestyle='--', label='Unstable Boundary')  # Horizontal line at y=1
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.7)  # Mirrored line for symmetry
plt.plot(a_values, stable_results, label='Stability Region')

# Customize plot elements
plt.xlabel('Value of a')
plt.ylabel('Stability (True/False)')
plt.title('Stability Plot for |a| < 1')
plt.grid(True)
plt.legend()

# Highlight the stable region (adjust color as needed)
plt.fill_between(a_values, 1, stable_results, color='lightgreen', alpha=0.3)

plt.show()   