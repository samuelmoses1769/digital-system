import numpy as np
import matplotlib.pyplot as plt

# Define parameters
start_time = 0  # Starting point of the ramp
end_time = 5  # Ending point of the ramp
slope = 2  # Slope of the ramp

# Create time axis
t = np.linspace(start_time, end_time, 100)  # Generate 100 evenly spaced points

# Define the ramp function
y = slope * (t - start_time)

# Plot the ramp
plt.plot(t, y)
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("Ramp Function")
plt.grid(True)

# Show the plot
plt.show()