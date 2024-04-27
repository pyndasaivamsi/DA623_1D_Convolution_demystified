import numpy as np
import matplotlib.pyplot as plt

# Function for 1D convolution
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

# In a real scenario, ECG signal data is used in place of synthetic ECG signal
fs = 1000  
t = np.arange(0, 1, 1/fs) 
f_ecg = 1
ecg_signal = 0.5 * np.sin(2 * np.pi * f_ecg * t)  # Synthetic ECG signal

# A smoothing kernel
kernel = np.ones(50) / 50  

# Perform convolution
convolved_signal = convolution_1d(ecg_signal, kernel)

t_out=np.linspace(0, 1, len(convolved_signal))
# Plot the original and convolved signals
plt.figure(figsize=(10, 5))
plt.plot(t, ecg_signal, label='Original Signal')
plt.plot(t_out, convolved_signal, label='Convolved Signal', linestyle='--')
plt.title('1-D Convolution of Synthetic ECG signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
