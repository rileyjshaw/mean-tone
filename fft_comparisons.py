from numpy import sin, linspace, pi, hanning
from pylab import plot, show, title, xlabel, ylabel, subplot, semilogy
from scipy import fft, arange
from scipy.fftpack import rfft, rfftfreq

def plotSpectrum(data, rate):
    sample_length = len(data)
    k = arange(sample_length)
    period = sample_length / rate
    freqs = (k / period)[range(sample_length / 2)] #right-side frequency range

    Y = (fft(data) / sample_length)[range(sample_length / 2)]

    semilogy(freqs, abs(Y), 'r') # plotting the spectrum

def myPlotSpectrum(data, rate):
    fourier = rfft(data)
    abs_fourier = abs(fourier)
    freqs = rfftfreq(len(fourier), 1.0 / rate)
    semilogy(freqs, abs_fourier)

Fs = 150.0;  # sampling rate
Ts = 1.0 / Fs; # sampling interval
t = arange(0,1,Ts) # time vector

ff = 5;   # frequency of the signal
y = sin(2*pi*ff*t)

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(y,Fs)
show()

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
myPlotSpectrum(y,Fs)
show()
