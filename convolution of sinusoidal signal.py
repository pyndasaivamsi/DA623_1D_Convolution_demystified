import numpy as np
import matplotlib.pyplot as plt

def convolution_1d(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length + kernel_length - 1
    output = np.zeros(output_length)

    for i in range(output_length):
      for j in range(kernel_length):
        if(i>=j and i-j>=0 and i-j<signal_length):
          output[i] += signal[i-j] * kernel[j]

    return output

# Generate a sinusoidal signal
t = np.linspace(0, 1, 1000)  # Time vector from 0 to 1 with 1000 points
frequency = 5  # Frequency of the sinusoidal signal
amplitude = 1  # Amplitude of the sinusoidal signal
sinusoidal_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Define a smoothing kernel
kernel = np.array([0.5, 0.5, 0.5])  # Smoothing kernel coefficients

# Perform convolution
convolved_signal = convolution_1d(sinusoidal_signal, kernel)

t_out=np.linspace(0, 1, len(convolved_signal))
# Plot the original and convolved signals
plt.figure(figsize=(10, 5))
plt.plot(t, sinusoidal_signal, label='Original Signal')
plt.plot(t_out, convolved_signal, label='Convolved Signal', linestyle='--')
plt.title('1-D Convolution of Sinusoidal Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()