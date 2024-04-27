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

# Generate a white noise signal
signal_length=100
white_noise= np.random.randn(signal_length)
t = np.linspace(0, 1, signal_length)  # Time vector from 0 to 1 with 100 points

# Define a smoothing kernel
kernel = np.array([0.5, 1, 0.2])  # Smoothing kernel coefficients

# Perform convolution
convolved_signal = convolution_1d(white_noise, kernel)

t_out=np.linspace(0, 1, len(convolved_signal))
# Plot the original and convolved signals
plt.figure(figsize=(10, 5))
plt.plot(t, white_noise, label='Original Signal')
plt.plot(t_out, convolved_signal, label='Convolved Signal', linestyle='--')
plt.title('1-D Convolution of White Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()