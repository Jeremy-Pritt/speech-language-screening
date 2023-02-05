import numpy as np
import librosa
from pydub import AudioSegment

def process_audio(uploaded_file):
    "200 mb limit for files"
    """
    Prepares MP3 and WAV files to be ready to be processed by ML models by extracting samples and sampling rate
    :param uploaded_file: will accept either a wav file or an mp3 file
    :return: two varialbes are returned; the first is an array of the samples and the second is the sampling rate
    """
    if uploaded_file is not None:
        if uploaded_file.name.endswith('wav'):
            x, sr = librosa.load(uploaded_file, sr=16000)
            samples_arry = np.array(x)
            return samples_arry, sr
        elif uploaded_file.name.endswith('mp3'):
            output_file = 'result.wav'
            sound = AudioSegment.from_mp3(uploaded_file)
            sound.export(output_file, format="wav")
            x, sr = librosa.load(output_file, sr=16000)
            samples_arry = np.array(x)
            return samples_arry, sr



# def process_audio(uploaded_file):
#     "200 mb limit for files"
#     """
#     Prepares MP3 and WAV files to be ready to be processed by ML models by extracting samples and sampling rate
#     :param uploaded_file: will accept either a wav file or an mp3 file
#     :return: two varialbes are returned; the first is an array of the samples and the second is the sampling rate
#     """
#     if uploaded_file is not None:
#         if uploaded_file.name.endswith('wav'):
#             audio = pydub.AudioSegment.from_wav(uploaded_file)
#             audio = audio.set_frame_rate(16000)
#             samples_arry = np.array(audio.get_array_of_samples())
#             sr = audio.frame_rate
#             return samples_arry, sr
#         elif uploaded_file.name.endswith('mp3'):
#             audio = pydub.AudioSegment.from_mp3(uploaded_file)
#             audio = audio.set_frame_rate(16000)
#             samples_arry = np.array(audio.get_array_of_samples())
#             sr = audio.frame_rate
#             return samples_arry, sr