import matplotlib.pyplot as plt
import numpy as np

def asymmetric_sawtooth(t, amplitude=1, period=1, slope_up=1, slope_down=1, phase=0):
    t_normalized = (t - phase) % period
    return amplitude * (t_normalized * slope_up / period - np.floor(t_normalized / period))

# Generate time values from 0 to 4 with a small interval
t = np.linspace(0, 4, 1000)

# Set the parameters for the asymmetric sawtooth waveform
amplitude = 1        # Amplitude of the sawtooth wave
period = 1           # Period of the sawtooth wave
slope_up = 2         # Slope of the rising edge
slope_down = -1      # Slope of the falling edge
phase = 0            # Phase shift of the sawtooth wave

# Calculate the asymmetric sawtooth waveform values
y = asymmetric_sawtooth(t, amplitude, period, slope_up, slope_down, phase)

# Plot the asymmetric sawtooth waveform
plt.plot(t, y, label='Asymmetric Sawtooth Waveform')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Asymmetric Sawtooth Waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()