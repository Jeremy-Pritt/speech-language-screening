from pyannote.audio import Pipeline
from mp3_to_wav import mp3_to_wav
import re
from pydub import AudioSegment
import streamlit as st


@st.cache_resource
def load_pipeline():
    return Pipeline.from_pretrained(
        'pyannote/speaker-diarization@2.1', use_auth_token="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")


def sec(timeStr):
    # quick helper function for making the output look cleaner
    spl = timeStr.split(":")
    s = (float)((int(spl[0]) * 60 * 60 +
                 int(spl[1]) * 60 + float(spl[2])))
    return s


def speech_diarization(uploaded_file):
    # import the pretrained diarization model
    pipeline = load_pipeline()

    # make sure that we are working with a wav file (not mp3)
    wav_file = mp3_to_wav(uploaded_file)

    # trim the audio to a given time constraint
    audio = AudioSegment.from_wav(wav_file)
    start_time = 0  # start at the beginning
    end_time = 1 * 60 * 1000  # end after 1 minute (in milliseconds)
    trimmed_audio = audio[start_time:end_time]
    trimmed_audio.export("temp_trimmed_file.wav", format="wav")

    # apply diarization pipeline to wav file
    diarization = pipeline("temp_trimmed_file.wav", num_speakers=2)

    # dump the diariztion output to a temp_file
    with open("temp_diarization.txt", "w") as text_file:
        text_file.write(str(diarization))

    print("List:")
    print(*list(diarization.itertracks(yield_label=True)), sep="\n")
    print("")

    dz = open('temp_diarization.txt').read().splitlines()
    dzList = []
    for l in dz:
        start, end = tuple(re.findall(
            '[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=l))
        start = sec(start)
        end = sec(end)
        lex = re.findall('SPEAKER_00', string=l)
        if lex == []:
            lex = re.findall('SPEAKER_01', string=l)

        dzList.append([(start, end), lex[0]])

    return dzList, r"temp_trimmed_file.wav"
