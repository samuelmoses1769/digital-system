import matplotlib.pyplot as plt
import numpy as np

def delta_function(t):
  """
  Implements the Dirac delta function δ(t).

  Args:
    t: A scalar or array of real numbers representing time values.

  Returns:
    A scalar or array with the same shape as t, containing a spike at t = 0 and 0 elsewhere.
  """
  return np.where(np.isclose(t, 0), np.inf, 0)

# Define time range and resolution
t_min, t_max = -5, 5
dt = 0.01
t = np.arange(t_min, t_max + dt, dt)

# Calculate delta function values
delta_values = delta_function(t)

# Plot the delta function
plt.plot(t, delta_values)
plt.xlabel("Time (t)")
plt.ylabel("δ(t)")
plt.title("Unit Impulse Function")
plt.xlim(t_min, t_max)
plt.ylim(-1, 1)  # Adjust y-axis limits to show the spike clearly
plt.grid(True)
plt.axvline(0, color="red", linestyle="--", linewidth=0.5, label="t = 0")
plt.legend()
plt.show()
