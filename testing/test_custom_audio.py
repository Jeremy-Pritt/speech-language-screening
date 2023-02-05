from transformers import WhisperProcessor, WhisperForConditionalGeneration
import pydub
from process_audio import process_audio
import numpy as np

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
model.config.forced_decoder_ids = None

# load dummy dataset and read audio files
audio = pydub.AudioSegment.from_file("test.wav")
audio = audio.set_frame_rate(16000)
samples_arry = np.array(audio.get_array_of_samples())
sr = audio.frame_rate




# wav_file = pydub.AudioSegment.from_file(file = "test.wav", format = "wav")
# samples_array, sr = process_audio(wav_file)
input_features = processor(samples_arry, sampling_rate=sr, return_tensors="pt").input_features


# generate token ids
predicted_ids = model.generate(input_features)
# decode token ids to text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)

print("start")
print(input_features)
print()
print(type(input_features))
print()

print("length:", len(samples_arry))
print("shape:", samples_arry.shape)


print()

print(transcription)

print("end")