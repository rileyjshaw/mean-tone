import numpy, scipy
import scipy.io.wavfile as wav

def repeater( chunk_size, song_data ):
    temp_data = []
    for i in range( 0, len( song_data ), chunk_size ):
        temp_data.extend( [ song_data[ i + a ] for a in range( chunk_size ) if ( i + a ) < len( song_data ) ] * 2 )
    return temp_data
