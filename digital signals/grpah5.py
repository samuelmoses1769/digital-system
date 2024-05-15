import matplotlib.pyplot as plt
import numpy as np

# Define parameters
T = 10  # Period of the pulse
w = 2 * np.pi / T  # Angular frequency
duty_cycle = 0.4  # Duty cycle (percentage of time the pulse is high)
t_min = 0  # Starting time
t_max = 4 * T  # Ending time (show 4 periods)

# Create time axis
t = np.linspace(t_min, t_max, 1000)

# Define the periodic rectangular pulse function
def rect_pulse(t, T, duty_cycle):
    return np.where((t % T) < duty_cycle * T, 1, 0)

# Calculate pulse values
y = rect_pulse(t, T, duty_cycle)

# Plot the pulse
plt.plot(t, y)
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("Periodic Rectangular Pulse")
plt.xlim(t_min, t_max)
plt.grid(True)
plt.show()