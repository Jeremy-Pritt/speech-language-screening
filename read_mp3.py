from audio2numpy import open_audio


def read_mp3(file):
    signal, sampling_rate = open_audio(file)
