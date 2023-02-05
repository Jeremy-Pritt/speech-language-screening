import streamlit as st
from st_custom_components import st_audiorec
from process_audio import process_audio
from whisper_predict_transcription import whisper_predict_transcription
from convert_bytes_to_wav import convert_bytes_to_wav


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
        age_year = st.selectbox(label="Years:", options=(
            "4", "5", "6", "7", "8", "9", "10", "11"))
        age_month = st.selectbox(label="Months:", options=(
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))
        submission = st.form_submit_button("Submit and Run Screening")
        if submission == True:
            # logic goes here for processing speech sample
            samples_arry, sampling_rate = process_audio(speech_sample)
            st.success("Speech Sample Successfully Processed")
            transcription = whisper_predict_transcription(samples_arry, sampling_rate)
            st.success("Transcription Successfully Processed:")
            st.success(transcription)




with mic_recording_tab:
    mic_recording_form = st.form('Make and Upload a Speech Sample')
    with mic_recording_form:
        speech_sample_mic = st_audiorec()
        st.write("Please enter your child's age:")
        age_year_mic = st.selectbox(label="Years:", options=(
            "4", "5", "6", "7", "8", "9", "10", "11"))
        age_month_mic = st.selectbox(label="Months:", options=(
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))
        submission_mic = st.form_submit_button("Submit and Run Screening")
        if submission_mic == True:

            convert_bytes_to_wav(speech_sample_mic)
            mic_input = "mic_input.wav"
            # logic goes here for processing speech sample
            samples_arry_mic, sampling_rate_mic = process_audio(mic_input)
            st.error("microphone functionality in progress")
            # logic goes here for processing speech sample
            # samples_arry_mic, sampling_rate_mic = process_audio(uploaded_file)
            st.success(type(speech_sample_mic))
            st.success(type(samples_arry_mic))
            st.success(type(sampling_rate_mic))
            st.success(samples_arry_mic)
            st.success(sampling_rate_mic)

