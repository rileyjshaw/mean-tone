import numpy
import scipy.io.wavfile as wav
import scipy.fftpack as fft

r, d = wav.read( "bass.wav" )

result = fft.fft( d )

print result[ 1 ]


