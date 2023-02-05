import pydub
import numpy as np


def process_audio(uploaded_file):
    "200 mb limit for files"
    """
    Prepares MP3 and WAV files to be ready to be processed by ML models by extracting samples and sampling rate
    :param uploaded_file: will accept either a wav file or an mp3 file
    :return: two varialbes are returned; the first is an array of the samples and the second is the sampling rate
    """
    if uploaded_file is not None:
        if uploaded_file.name.endswith('wav'):
            audio = pydub.AudioSegment.from_wav(uploaded_file)
            #audio = audio.set_frame_rate(16000)
            samples_arry = np.array(audio.get_array_of_samples())
            sr = audio.frame_rate
            return samples_arry, sr
        elif uploaded_file.name.endswith('mp3'):
            audio = pydub.AudioSegment.from_mp3(uploaded_file)
            audio = audio.set_frame_rate(16000)
            samples_arry = np.array(audio.get_array_of_samples())
            sr = audio.frame_rate
            return samples_arry, sr