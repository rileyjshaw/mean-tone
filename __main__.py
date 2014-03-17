import numpy as np, composer
import scipy.io.wavfile as wav
import scipy.fftpack as fft
from itertools import izip_longest

import_rate, import_data = wav.read('wav/flute.wav')
import_bpm = 62 #manually set

def grouper(iterable, n, fillvalue = None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue = fillvalue, *args)

def average_frequency(rate, data):
    sample_length = len(data)
    k = np.arange(sample_length)
    period = sample_length / rate
    freqs = (k / period)[range(sample_length / 2)] #right-side frequency range
    fourier = abs(fft.fft(data * np.hanning(sample_length)) / sample_length)[range(sample_length / 2)] #normalize & clip to right side
    power = np.power(fourier, 2.0)
    return sum(power * freqs) / sum(power)

def quarter_note_frequencies(rate, data, bpm):
    notes = []
    beat_counter = 0
    slice_size = rate * 60 / bpm #samples per beat
    beats = len(data) / slice_size #beats per song
    for slice in grouper(data, slice_size, 0):
        beat_counter += 1
        print unicode(beat_counter * 100 / beats) + '% completed'
        notes.append(average_frequency(rate * 1.0, slice))
    return notes

def create_wav(rate, data, bpm):
    duration = 60.0 / bpm #seconds per beat
    wav.write('wav/flute_avg.wav', rate, np.array(composer.generate_tone_series(data, duration), dtype = np.int16))

create_wav(import_rate, quarter_note_frequencies(import_rate, import_data, import_bpm), import_bpm)
