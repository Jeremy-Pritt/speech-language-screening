from pydub import AudioSegment


def mp3_to_wav(uploaded_file):
    if uploaded_file is not None:
        if hasattr(uploaded_file, 'name'):
            if uploaded_file.name.endswith('wav'):
                output_file = uploaded_file
                return output_file
            elif uploaded_file.name.endswith('mp3'):
                output_file = 'temp_result.wav'
                sound = AudioSegment.from_mp3(uploaded_file)
                sound.export(output_file, format="wav")
                return output_file
        else:
            if uploaded_file.endswith('wav'):
                output_file = uploaded_file
                return output_file
            elif uploaded_file.endswith('mp3'):
                output_file = 'temp_result.wav'
                sound = AudioSegment.from_mp3(uploaded_file)
                sound.export(output_file, format="wav")
                return output_file
