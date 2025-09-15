'''a.	Generate two sine wave signals with frequencies of 5 Hz and 10 Hz
both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.'''
# import numpy as np
# import matplotlib.pyplot as plt

# sampling_rate = 1000  
# duration = 1          
# frequency1 = 5        
# frequency2 = 10       


# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# signal1 = np.sin(2 * np.pi * frequency1 * t)
# signal2 = np.sin(2 * np.pi * frequency2 * t)

# combined_signal = signal1 + signal2
# plt.figure(figsize=(12, 6)) 
# plt.plot(t, combined_signal, label='Combined Signal (5 Hz + 10 Hz)')
# plt.title('Combined Sine Wave Signals')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend()
# plt.show()








'''b.	Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. 
Multiply the two signals element-wise and plot the resulting signal.'''


# import numpy as np
# import matplotlib.pyplot as plt

# sampling_rate = 500           
# frequency_sine = 5    
# frequency_cosine = 10 
# duration = 2

# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# sine_signal = np.sin(2 * np.pi * frequency_sine * t)
# cosine_signal = np.cos(2 * np.pi * frequency_cosine * t)

# resulting_signal = sine_signal * cosine_signal

# plt.figure(figsize=(12, 6)) 
# plt.plot(t, resulting_signal, label='Resulting Signal (5 Hz Sine x 10 Hz Cosine)')
# plt.title('Multiplication of Sine and Cosine Wave Signals')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend()

# plt.show()










'''Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds.

Plot the original and shifted signals on the same graph for comparison.'''


# import numpy as np
# import matplotlib.pyplot as plt

# sampling_rate = 500   
# duration = 2          
# frequency = 5         
# time_shift = 0.1      

# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# original_signal = np.sin(2 * np.pi * frequency * t)

# shifted_signal = np.sin(2 * np.pi * frequency * (t - time_shift))

# plt.figure(figsize=(12, 6))
# plt.plot(t, original_signal, label='Original Sine Wave (5 Hz)', color='blue')
# plt.plot(t, shifted_signal, label=f'Shifted Sine Wave (+{time_shift} s)', color='red', linestyle='--')

# plt.title('Original vs. Time-Shifted Sine Wave Signals')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend()
# plt.show()







'''Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot
the original and scaled signals together.'''


# import numpy as np
# import matplotlib.pyplot as plt

# sampling_rate = 500   
# duration = 2          
# frequency = 10       
# amplitude_scale = 3  

# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# original_signal = np.sin(2 * np.pi * frequency * t)
# scaled_signal = amplitude_scale * original_signal
# plt.figure(figsize=(12, 6)) 
# plt.plot(t, original_signal, label='Original Signal (Amplitude = 1)', color='blue')
# plt.plot(t, scaled_signal, label=f'Scaled Signal (Amplitude = {amplitude_scale})', color='red', linestyle='--')
# plt.title('Original vs. Amplitude-Scaled Sine Wave Signals')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend()

# plt.show()










'''Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. '''
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 500   
duration = 2         
frequency = 5        

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

original_signal = np.sin(2 * np.pi * frequency * t)

reversed_signal = original_signal[::-1]

plt.figure(figsize=(12, 6))
plt.plot(t, original_signal, label='Original Signal', color='blue')
plt.plot(t, reversed_signal, label='Time-Reversed Signal', color='red', linestyle='--')

plt.title('Original vs. Time-Reversed Sine Wave Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()


plt.show()