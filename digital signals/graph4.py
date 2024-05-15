import matplotlib.pyplot as plt
import numpy as np

# Define parameters
w = 2 * np.pi  # Angular frequency (adjust as needed)
t_min = 0  # Starting time
t_max = 10  # Ending time

# Create time axis
t = np.linspace(t_min, t_max, 1000)  # Generate 1000 evenly spaced points

# Calculate y values using the sine function
y = np.sin(w * t)

# Plot the graph
plt.plot(t, y)
plt.xlabel("Time (t)")
plt.ylabel("y")
plt.title("Graph of y = sin(wt)")
plt.xlim(t_min, t_max)  # Set appropriate x-axis limits
plt.grid(True)

# Show the plot
plt.show()