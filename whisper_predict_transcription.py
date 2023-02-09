import torch
from transformers import pipeline

def whisper_predict_transcription(samples_array, sampling_rate):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny",
        chunk_length_s=30,
        device=device,
    )
    sample = {}
    sample['array'] = samples_array
    sample['sampling_rate'] = sampling_rate

    # transcription = pipe(sample)["text"]
    transcription = pipe(sample, return_timestamps=True)["chunks"]
    return transcription


# def whisper_predict_transcription(samples_array, sampling_rate, language="english"):
#     """
#     Outputs the predicted transcription using whisper-tiny model
#     :param samples_array: numpy array of samples from audio file
#     :param sampling_rate: sampling rate of the audio file
#     :return: predicted transcription based off of whisper model
#     """
#     # load model and processor
#     processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
#     model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
#     model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language=language, task="transcribe")
#
#     input_features = processor(samples_array, sampling_rate=sampling_rate, return_tensors="pt").input_features
#
#     predicted_ids = model.generate(inputs=input_features)
#
#     transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
#
#     return transcription

