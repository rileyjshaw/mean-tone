import math
import numpy as np
import scipy.io.wavfile as wav

sentinel = object()
sin = lambda f, t, sr: math.sin( 2 * math.pi * t * f / sr )

# !1,3,6,8,10
notes = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 9,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11
}

def generate_frequency ( note, octave, accidental ):
    f = 2
    pitch = 69 + 12 * np.log2( f / 440 )
    #note -

def generate_chord ( frequencies, duration, max_volume, sustain_volume = sentinel, sample_rate = 44100, adr = sentinel ):
    if sustain_volume == sentinel:
        sustain_volume = max_volume * 0.6
    if adr == sentinel:
        adr = [ duration * 0.05, duration * 0.05, duration * 0.2 ]

    duration *= sample_rate
    attack = sample_rate * adr[ 0 ]
    decay = sample_rate * adr[ 1 ]
    release = sample_rate * adr[ 2 ]
    sustain = duration - attack - decay - release

    if ( sustain < 0 ):
        raise AttributeError( "Total of attack, decay, and release values is greater than duration")

    try:
        len( frequencies )
    except TypeError as e:
        frequencies = [ frequencies ]

    def frequencies_to_floats ( f ):
        try:
            return f * 1.0
        except TypeError as e:
            return generate_frequency( f )

    frequencies = map(frequencies_to_floats, frequencies)

    tone = []
    d_start = attack
    s_start = d_start + decay
    r_start = s_start + sustain

    s_drop_factor = 1.0 - sustain_volume / max_volume

    a_envelope = lambda accum, f: accum + sin( f, t, sample_rate ) * max_volume * t / attack
    for t in np.arange( attack ):
        tone.append( reduce( a_envelope, frequencies, 0 ) )

    d_envelope = lambda accum, f: accum + sin( f, d_start + t, sample_rate ) * max_volume * ( 1 - s_drop_factor * t / decay )
    for t in np.arange( decay ):
        tone.append( reduce( d_envelope, frequencies, 0 ) )

    s_envelope = lambda accum, f: accum + sin( f, s_start + t, sample_rate ) * sustain_volume
    for t in np.arange( sustain ):
        tone.append( reduce( s_envelope, frequencies, 0 ) )

    r_envelope = lambda accum, f: accum + sin( f, r_start + t, sample_rate ) * sustain_volume * ( 1 - t / release )
    for t in np.arange( release ):
        tone.append( reduce( r_envelope, frequencies, 0 ) )

    return tone

def generate_song(chord_list):
    return reduce(lambda accum, current: accum + generate_chord( *current ), chord_list, [])

def generate_tone_series(data, duration):
    chord_list = []
    for tone in data:
        chord_list.append([tone, duration, 6000])
    return generate_song(chord_list)

'''
#Usage example:

song = [ [ ['A', 130.81], 30.0, 6000, 5000, 44100, [0.2, 0.2, 0.2] ],
          [ [1760.0, 1600.0, 1660.0], 0.5, 8000, 6000, 44100, [0.2, 0.05, 0.2] ],
          [ [110.0, 130.81], 30.0, 6000, 5000, 44100, [0.2, 0.2, 0.2] ] ]

# wav.write('sin_original.wav', 44100, np.array(generate_song(song), dtype = np.int16 ) )
## Generate a440
wav.write('a440.wav', 44100, np.array(generate_chord(440, 10, 4000), dtype = np.int16))
## Plot wave
# pl.plot(np.array(generate_chord(440, 10, 4000)))
# pl.show()
'''