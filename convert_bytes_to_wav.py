import io
from pydub import AudioSegment

def convert_bytes_to_wav(raw_sound):
    s = io.BytesIO(raw_sound)
    filename = "mic_input.wav"
    audio = AudioSegment.from_raw(s).export(filename, format='wav')
    return audio