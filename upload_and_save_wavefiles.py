import pydub
from pathlib import Path
import ffprobe


def upload_and_save_wavefiles(uploaded_file):
    """ limited 200MB, you could increase by `streamlit run foo.py --server.maxUploadSize=1024` """
    if uploaded_file is not None:
        if uploaded_file.name.endswith('wav'):
            audio = pydub.AudioSegment.from_wav(uploaded_file)
            file_type = 'wav'
        elif uploaded_file.name.endswith('mp3'):
            audio = pydub.AudioSegment.from_mp3(uploaded_file)
            file_type = 'mp3'
    return audio
