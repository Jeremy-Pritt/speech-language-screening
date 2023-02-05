import wave

def convert_bytes_to_wav(raw_sound):
    with open(raw_sound, "rb") as inp_f:
        data = inp_f.read()
        with wave.open("mic_input.wav", "wb") as out_f:
            out_f.setnchannels(1)
            out_f.setsampwidth(2) # number of bytes
            out_f.setframerate(16000)
            out_f.writeframesraw(data)
    return None