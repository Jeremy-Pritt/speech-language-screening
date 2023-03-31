import json
import os
import pandas as pd


def process_children_data(transcription):
    
    df = pd.DataFrame([transcription], columns=['transcription'])

    df['transcription'] = df['transcription'].apply(lambda x: [item['text'] for item in x])

    df['numberofutterance'] = df['transcription'].apply(lambda x: len(x))

    df['wordsInEachUtterance'] = df['transcription'].apply(lambda x: [len(item.split()) for item in x])
    
    df['avgWordsPerUtterance'] = df['wordsInEachUtterance'].apply(lambda x: sum(x) / len(x))
    
    df.drop(['transcription', 'wordsInEachUtterance'], axis=1, inplace=True)

    return df