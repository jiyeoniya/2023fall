import librosa
import numpy as np
import matplotlib.pyplot as plt


y, sr = librosa.load('audio3.mp3')

fft_result = np.fft.fft(y)

freq = np.fft.fftfreq(len(y), 1/sr)

plt.plot(freq, np.abs(fft_result))
plt.show()
