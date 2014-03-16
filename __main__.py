import pylab as pl
import numpy as np
import scipy.io.wavfile as wav
import scipy.fftpack as fft
import composer
from itertools import izip_longest

def grouper(iterable, n, fillvalue = None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue = fillvalue, *args)

def average_frequency(rate, data):
    fourier = fft.rfft((data * np.hanning(len(data))))
    abs_fourier = np.abs(fourier)
    power = np.power(fourier, 2.0)
    freqs = fft.rfftfreq(len(fourier), 1.0 / rate)
    return sum(power * freqs) / sum(power)

def median_frequency(rate, data):
    return 0

def quarter_note_frequencies(rate, data, bpm):
    notes = []
    beat_counter = 0
    slice_size = rate * 60 / bpm #samples per beat
    beats = len(data) / slice_size #beats per song
    for slice in grouper(data, slice_size, 0):
        beat_counter += 1
        print unicode(beat_counter * 100 / beats) + '% completed'
        notes.append(average_frequency(rate, slice))
    return notes

def create_wav(rate, data, bpm):
    chord_list = []
    duration = 60.0 / bpm #seconds per beat
    for beat in data:
        chord_list.append([beat, duration, 6000])
    wav.write('demo.wav', rate, np.array(composer.generate_song(chord_list), dtype = np.int16))

import_rate, import_data = wav.read('flute.wav')
import_bpm = 62

create_wav(import_rate, quarter_note_frequencies(import_rate, import_data, import_bpm), import_bpm)

#pl.semilogy(freqs, abs_fourier)
#pl.show()
