# Convolution of two 1-D signals

# Convolution operation
def convolution_1d(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length + kernel_length - 1
    output = [0] * output_length

    for i in range(output_length):
      for j in range(kernel_length):
        if(i>=j and i-j>=0 and i-j<signal_length):
          output[i] += signal[i-j] * kernel[j]

    return output

# 1-D Signals
signal = [1, 2, 3, 4, 5]
kernel = [0.5, 1, 0.5]

convolved_signal = convolution_1d(signal, kernel)
print(convolved_signal)
