import numpy
import scipy.io.wavfile as wav
import scipy.fftpack.fft as fft

r, d = wav.read( "bass.wav" )

def slowdown_keep_pitch_naive( chunk_size, song_data ):
    temp_data = []
    for i in range( 0, len( song_data ), chunk_size ):
        temp_data.extend( [ song_data[ i + a ] for a in range( chunk_size ) if ( i + a ) < len( song_data ) ] * 2 )
    return numpy.array(temp_data)

wav.write( "really_naive", r / 2, song_data )
wav.write( "naive.wav", r, slowdown_keep_pitch_naive( 5, d ) )
