import soundfile as sf
import io

def convert_sound_bytes(bytes_arry):
    samples_arry, sr = sf.read(io.BytesIO(bytes_arry))
    return samples_arry, sr
