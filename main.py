import pandas as pd
import numpy as np
import streamlit as st
from st_custom_components import st_audiorec


st.title("Speech-Language Screening")

tabs = st.tabs(["Upload Recording", "Make a New Recording"])
pre_recorded_tab = tabs[0]
new_recording_tab = tabs[1]

with pre_recorded_tab:
    pre_recorded_form = st.form("Upload a Speech Sample")
    with pre_recorded_form:
        speech_sample = st.file_uploader("Please upload an audio file of your child\'s speech:")
        age = st.text_input("Please enter your child's age:")
        submission = st.form_submit_button("Submit and Run Screening")

with new_recording_tab:
    new_recording_form = st.form('Make and Upload a Speech Sample')
    with new_recording_form:
        wav_audio_data = st_audiorec()
        if wav_audio_data is not None:
            st.audio(wav_audio_data, format='audio/wav')
        age_new = st.text_input("Please enter your child\'s age:")
        submission_new = st.form_submit_button("Submit and Run Screening")



