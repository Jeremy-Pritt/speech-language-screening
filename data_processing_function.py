import pandas as pd
import numpy as np

# transciption = [
#     {'text1': 'I said something', 'timestamps': (0.0, 2.0)},
#     {'text2': 'I said something', 'timestamps': (0.0, 2.0)},
# ]

def process_children_data(transcription):
    transcription_str = ""
    for i in range(len(transcription)):
        if i == len(transcription) - 1:
            transcription_str += transcription[i]['text']
        else:
            transcription_str += transcription[i]['text']
            transcription_str += "NEW_UTTERANCE_STARTS_HERE"

    number_of_utterance = transcription_str.count(
        "NEW_UTTERANCE_STARTS_HERE") + 1

    splits = transcription_str.split("NEW_UTTERANCE_STARTS_HERE ")
    for i in range(len(splits)):
        if i == 0:
            splits[i] = splits[i][1:]

    words_in_each_utterance = np.mean([len(i.split(" ")) for i in splits])

    df = pd.DataFrame([[number_of_utterance, words_in_each_utterance]], columns=[
                      "numberofutterance", "avgWordsPerUtterance"])

    return df

    # print("transcription:", transcription)
    # print("transcription type:", str(type(transcription)))

    # df = pd.DataFrame([transcription], columns=['transcription'])

    # df['transcription'] = df['transcription'].apply(lambda x: [item['text'] for item in x])

    # df['numberofutterance'] = df['transcription'].apply(lambda x: len(x))

    # df['wordsInEachUtterance'] = df['transcription'].apply(lambda x: [len(item.split()) for item in x])

    # df['avgWordsPerUtterance'] = df['wordsInEachUtterance'].apply(lambda x: sum(x) / len(x))

    # df.drop(['transcription', 'wordsInEachUtterance'], axis=1, inplace=True)
