from transformers import WhisperProcessor, WhisperForConditionalGeneration

def whisper_predict_transcription(samples_array, sampling_rate):
    """
    Outputs the predicted transcription using whisper-tiny model
    :param samples_array: numpy array of samples from audio file
    :param sampling_rate: sampling rate of the audio file
    :return: predicted transcription based off of whisper model
    """
    # load model and processor
    processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
    model.config.forced_decoder_ids = None

    input_features = processor(samples_array, sampling_rate, return_tensors="pt")

    predicted_ids = model.generate(input_features)

    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

    return transcription

