# Low-pass FIR Filter with Rectangular Window
'''
Input a sequence of real numbers (finite length)
Input the sampling frequency and the desired cut-off frequency
fc = desired_cut-off_freq / sampling_freq

Ideal impulse response hi(n) = sin(2*pi*fc*n) / pi*n  when n != 0
							= 2*fc  when n = 0
Impulse response h(n) = hi(n).w(n)  here w(n) is the windowing function

In this code the windowing funtion is the Rectangular funciton
	w(n) = 1 for 0<=n<=N-1  N is the filter length

Now, y(n) = h * x
	* is the convultion operator
'''

import numpy as np
import matplotlib.pyplot as plt

#sampling frequency
Fs = 1000;
# cut-off frequency
Fc = 400;
# normalized cut-off frequency
fc = Fc/Fs;

# filter length
N = 15

n = np.arange(-(N+1)/2+1, (N+1)/2)
hi = np.sinc(2*fc*n)
hi /= np.sum(hi)
print(hi)

plt.stem(n, hi)
plt.title("Impulse Response of Low-Pass FIR Filter (Rectangular Window)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
step_signal = np.ones(100)
input_signal = np.sin(2 * np.pi * 0.05 * np.arange(100))  # Example input signal
output_signal = np.convolve(step_signal, hi, mode='full')

plt.subplot(2, 1, 1)
plt.plot(step_signal)
plt.title("Input Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(output_signal)
plt.title("Output Signal After Filtering")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
