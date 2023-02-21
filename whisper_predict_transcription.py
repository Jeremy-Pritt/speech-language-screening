import torch
from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_pipeline():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    return pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny",
        chunk_length_s=30,
        device=device,
    )


def whisper_predict_transcription(samples_array, sampling_rate):
    pipe = load_pipeline()
    sample = {}
    sample['array'] = samples_array
    sample['sampling_rate'] = sampling_rate

    # transcription = pipe(sample)["text"]
    transcription = pipe(sample, return_timestamps=True)["chunks"]
    return transcription
