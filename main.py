import streamlit as st
from st_custom_components import st_audiorec
from process_audio import process_audio
from whisper_predict_transcription import whisper_predict_transcription
from convert_bytes_to_wav import convert_bytes_to_wav
from speech_diarization import speech_diarization
from get_child_speech import get_child_speech
from data_processing_function import process_children_data
import pickle
import urllib.request

st.title("Speech-Language Screening")

tabs = st.tabs(["Upload Recording", "Use Microphone"])
pre_recorded_tab = tabs[0]
mic_recording_tab = tabs[1]

with pre_recorded_tab:
    pre_recorded_form = st.form("Upload a Speech Sample")
    with pre_recorded_form:
        speech_sample = st.file_uploader(
            "Please upload an audio file of your child\'s speech:", type=['wav', 'mp3'], accept_multiple_files=False)
        st.write("Please enter your child's age:")
        age_year = st.selectbox(label="Years:", options=("1", "2", "3",
                                                         "4", "5", "6", "7", "8", "9", "10", "11"))
        age_month = st.selectbox(label="Months:", options=(
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))

        gender = st.selectbox(label='Gender:', options=('Male', 'Female'))

        child_first_speaker = st.selectbox(label="Who is the first speaker in the recording?", options=(
            "The child", "The prompter (ie parent or SLP)"))
        submission = st.form_submit_button("Submit and Run Screening")

        if submission == True:

            age_year = int(age_year)
            age_month = int(age_month)

            if gender == "Male":
                gender = 1
            else:
                gender = 0

            # child_first_speaker logic
            if child_first_speaker == "The child":
                child_first = True
            else:
                child_first = False

            # logic for speech diarization
            with st.spinner("Isolating child's speech..."):
                dzList, trimmed_audio = speech_diarization(speech_sample)
                child_speech_sample = get_child_speech(dzList, trimmed_audio,
                                                       first_speaker_is_child=child_first)
                st.success("Successfully separated out child's speech")

            # logic goes here for transcribing speech
            with st.spinner("Processing speech..."):
                samples_arry, sampling_rate = process_audio(
                    child_speech_sample)
            st.success("Speech Sample Successfully Processed")
            with st.spinner("Building transcription..."):
                transcription = whisper_predict_transcription(
                    samples_arry, sampling_rate)
            st.success("Transcription Successfully Processed:")
            st.success(transcription)

            # add logic for making final prediction using RF model
            df = process_children_data(transcription)
            df['years_old'] = age_year
            df['months_old'] = age_month
            df['sex'] = gender
            df = df.reindex(columns=[
                            'utterances', 'words_per_utterance', 'sex', 'years_old', 'months_old'])

            # Set the URL of the public S3 bucket object
            url = 'https://speech-disorder-screening-public.s3.us-west-1.amazonaws.com/models/final_rf.pkl'

            # Download the object
            urllib.request.urlretrieve(url, 'final_rf.pickle')

            # Load the pickle object from the file
            with open('final_rf.pickle', 'rb') as f:
                model = pickle.load(f)
                prediction = model.predict(df)
                if prediction[0] == 'LT':
                    st.success("Result: Your child did NOT pass the screening and may be at risk for a language disorder. It is recommended that a speech-therapist evaluate your child to determine whether a language disorder is present.")
                else:
                    st.success(
                        "Result: Your child passed the screening. The screening did not detect that your child is at risk for a language disorder.")


with mic_recording_tab:
    mic_recording_form = st.form('Make and Upload a Speech Sample')
    with mic_recording_form:
        speech_sample_mic = st_audiorec()
        st.write("Please enter your child's age:")
        age_year_mic = st.selectbox(label="Years:", options=(
            "4", "5", "6", "7", "8", "9", "10", "11"))
        age_month_mic = st.selectbox(label="Months:", options=(
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))
        gender_mic = st.selectbox(label='Gender:', options=('Male', 'Female'))

        child_first_speaker_mic = st.selectbox(label="Who is the first speaker in the recording?", options=(
            "The child", "The prompter (ie parent or SLP)"))
        submission_mic = st.form_submit_button("Submit and Run Screening")
        if submission_mic == True:
            mic_input = convert_bytes_to_wav(speech_sample_mic)

            age_year_mic = int(age_year_mic)
            age_month_mic = int(age_month_mic)

            if gender_mic == "Male":
                gender_mic = 1
            else:
                gender_mic = 0

            # child_first_speaker logic
            if child_first_speaker_mic == "The child":
                child_first_mic = True
            else:
                child_first_mic = False

            # logic for speech diarization
            with st.spinner("Isolating child's speech..."):
                dzList_mic, trimmed_audio_mic = speech_diarization(mic_input)
                child_speech_sample_mic = get_child_speech(dzList_mic, trimmed_audio_mic,
                                                           first_speaker_is_child=child_first_mic)
            st.success("Successfully separated out child's speech")

            # logic for transcribing speech
            with st.spinner("Processing speech..."):
                samples_arry_mic, sampling_rate_mic = process_audio(
                    child_speech_sample_mic)
            st.success("Speech Sample Successfully Processed")
            with st.spinner("Building transcription..."):
                transcription_mic = whisper_predict_transcription(
                    samples_arry_mic, sampling_rate_mic)
            st.success("Transcription Successfully Processed:")
            st.success(transcription_mic)

            # add logic for making final prediction using RF model
            df_mic = process_children_data(transcription)
            df_mic['years_old'] = age_year_mic
            df_mic['months_old'] = age_month_mic
            df_mic['sex'] = gender_mic
            df_mic = df_mic.reindex(columns=[
                                    'utterances', 'words_per_utterance', 'sex', 'years_old', 'months_old'])

            # Set the URL of the public S3 bucket object
            url = 'https://speech-disorder-screening-public.s3.us-west-1.amazonaws.com/models/final_rf.pkl'

            # Download the object
            urllib.request.urlretrieve(url, 'final_rf.pickle')

            # Load the pickle object from the file
            with open('final_rf.pickle', 'rb') as f:
                model_mic = pickle.load(f)
                prediction_mic = model_mic.predict(df)
                if prediction_mic[0] == 'LT':
                    st.success("Result: Your child did NOT pass the screening and may be at risk for a language disorder. It is recommended that a speech-therapist evaluate your child to determine whether a language disorder is present.")
                else:
                    st.success(
                        "Result: Your child passed the screening. The screening did not detect that your child is at risk for a language disorder.")
