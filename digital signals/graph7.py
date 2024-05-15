import matplotlib.pyplot as plt
import numpy as np

# Define parameters
T = 10  # Period of the pulse
sigma = 2  # Standard deviation of the Gaussian
t_min = -2 * T  # Starting time
t_max = 3 * T  # Ending time

# Create time axis
t = np.linspace(t_min, t_max, 1000)

# Define the periodic Gaussian pulse function
def periodic_gaussian(t, T, sigma):
    return np.exp(-((t % T) / sigma) ** 2)

# Calculate pulse values
y = periodic_gaussian(t, T, sigma)

# Plot the pulse
plt.plot(t, y)
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("Periodic Gaussian Pulse")
plt.xlim(t_min, t_max)
plt.grid(True)
plt.show()