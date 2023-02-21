from mp3_to_wav import mp3_to_wav
from pydub import AudioSegment


def get_child_speech(dr_list, audio_file, first_speaker_is_child=False):

    # make sure that we are working with a wave file (not mp3 file)
    audio_file = mp3_to_wav(audio_file)

    # initialize list of the child's utterances
    child_utterance_segments = []

    # find the label for the first speaker
    first_speaker = dr_list[0][1]

    # logic for if the first speaker is the child
    if first_speaker_is_child == True:
        for segment in dr_list:
            if segment[1] == first_speaker:
                child_utterance_segments.append(
                    (segment[0][0] - .05, segment[0][1] + .05))
            else:
                continue

    # logic for if the second speaker is the child
    else:
        for segment in dr_list:
            if segment[1] == first_speaker:
                continue
            else:
                child_utterance_segments.append(
                    (segment[0][0] - .05, segment[0][1] + .05))

    print(child_utterance_segments)

    audio = AudioSegment.from_wav(audio_file)
    spacermilli = 2000
    spacer = AudioSegment.silent(duration=spacermilli)
    audio = spacer.append(audio, crossfade=0)
    audio.export("temp_audio.wav", format='wav')

    # load the audio file into a pydub AudioSegment object
    audio = AudioSegment.from_file(audio_file)

    # Concatenate the child's speech segments into a new audio data object with 2 seconds of silence between each segment
    new_audio = AudioSegment.silent(duration=2000)
    for i, segment in enumerate(child_utterance_segments):
        start_time = (segment[0]) * 1000
        end_time = (segment[1]) * 1000

        segment_audio = audio[start_time:end_time]
        new_audio = new_audio + segment_audio
        if i < len(child_utterance_segments) - 1:
            # add 2 seconds of silence between segments
            new_audio = new_audio + AudioSegment.silent(duration=2000)

    output_file = "temp_child_only.wav"
    new_audio.export(output_file, format="wav")

    return output_file
