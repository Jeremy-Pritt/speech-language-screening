import io
from pydub import AudioSegment

def convert_bytes_to_wav(raw_sound):
    s = io.BytesIO(raw_sound)
    filename = "mic_input.wav"
    audio = AudioSegment.from_raw(s, sample_width=4, frame_rate=44100, channels=2).export(filename, format='wav')
    return audio