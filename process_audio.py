import librosa


def process_audio(uploaded_file):
    "200 mb limit for files"
    """
    Prepares MP3 and WAV files to be ready to be processed by ML models by extracting samples and sampling rate
    :param uploaded_file: will accept either a wav file or an mp3 file
    :return: two varialbes are returned; the first is an array of the samples and the second is the sampling rate
    """
    if uploaded_file is not None:
        if uploaded_file.name.endswith('wav'):
            samples_arry, sr = librosa.load(uploaded_file, sr=16000)
            return samples_arry, sr
        elif uploaded_file.name.endswith('mp3'):
            samples_arry, sr = librosa.load(uploaded_file, sr=16000)
            return samples_arry, sr
