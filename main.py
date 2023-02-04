import pandas as pd
import numpy as np
import streamlit as st
from st_custom_components import st_audiorec
from read_mp3 import read_mp3
import os
from upload_and_save_wavefiles import upload_and_save_wavefiles


st.title("Speech-Language Screening")

tabs = st.tabs(["Upload Recording", "Make a New Recording"])
pre_recorded_tab = tabs[0]
new_recording_tab = tabs[1]

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

            audio_seg = upload_and_save_wavefiles(speech_sample)

            st.success(audio_seg)
            # signal, sampling_rate = read_mp3(speech_sample)
            #
            # st.success('signal:', signal)
            # st.success("sampling_rate:", sampling_rate)

with new_recording_tab:
    new_recording_form = st.form('Make and Upload a Speech Sample')
    with new_recording_form:
        speech_sample_new = st_audiorec()
        if speech_sample_new is not None:
            st.audio(speech_sample_new, format='audio/wav')
        st.write("Please enter your child's age:")
        age_year_new = st.selectbox(label="Years:", options=(
            "4", "5", "6", "7", "8", "9", "10", "11"))
        age_month_new = st.selectbox(label="Months:", options=(
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))
        submission_new = st.form_submit_button("Submit and Run Screening")
        if submission_new == True:
            # logic goes here for processing speech sample
            audio_seg_bytes = speech_sample_new
            st.success(audio_seg_bytes)
