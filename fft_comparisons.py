import numpy as np
import composer
from pylab import plot, show, title, xlabel, ylabel, subplot, semilogy
from scipy import fft, arange
from scipy.fftpack import rfft, rfftfreq
import scipy.io.wavfile as wav

def standard_plot(data, rate):
    sample_length = len(data)
    k = arange(sample_length)
    period = sample_length / rate
    freqs = (k / period)[range(sample_length / 2)] #right-side frequency range
    Y = (fft(data) / sample_length)[range(sample_length / 2)]
    semilogy(freqs, abs(Y)) # plotting the spectrum

def hanning_standard_plot(data, rate):
    sample_length = len(data)
    k = arange(sample_length)
    period = sample_length / rate
    freqs = (k / period)[range(sample_length / 2)] #right-side frequency range
    Y = (fft(data * np.hanning(sample_length)) / sample_length)[range(sample_length / 2)]
    semilogy(freqs, abs(Y))

def real_plot(data, rate):
    fourier = rfft(data)
    abs_fourier = abs(fourier)
    freqs = rfftfreq(len(fourier), 1.0 / rate)
    semilogy(freqs, abs_fourier)

def hanning_real_plot(data, rate):
    fourier = rfft(data * np.hanning(len(data)))
    abs_fourier = abs(fourier)
    freqs = rfftfreq(len(fourier), 1.0 / rate)
    semilogy(freqs, abs_fourier)

single_tone = np.array(composer.generate_tone_series([440], 1), dtype = np.int16)
series_tone = np.array(composer.generate_tone_series([100, 200, 400, 800, 1600], 1), dtype = np.int16)
chord_tone = np.array(composer.generate_tone_series([[330, 440]], 1), dtype = np.int16)
song_rate, song = wav.read('wav/bass.wav')

for audio in [single_tone, series_tone, chord_tone, song]:
    for method in [standard_plot, hanning_standard_plot, real_plot, hanning_real_plot]:
        subplot(2, 1, 1)
        plot(audio)
        xlabel('Time')
        ylabel('Amplitude')
        subplot(2, 1, 2)
        method(audio, rate)
        show()
