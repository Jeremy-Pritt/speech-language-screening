import json

import pandas as pd
import s3fs
from sklearn.model_selection import train_test_split

from data_processing_function import process_children_data

LT = 'speech-disorder-screening/transcripts/whisper/LT'
TD = 'speech-disorder-screening/transcripts/whisper/TD'

creds = json.load(open('aws_creds.txt', 'r'))
fs = s3fs.S3FileSystem(username=creds['id'], password=creds['secret'])

# CAREFUL; AS OF WRITING THIS COMMENT, THE COLUMNS ARE MISALIGNED FOR AGE AND SEX
# metadata = pd.read_csv('language_disorders.csv')
# metadata['subpath'] = metadata['path_to_transcript'].apply(lambda s: s.replace('/', '-') + '.json')

data = {
    'raw': [],
    'numberofutterance': [],
    'avgWordsPerUtterance': [],
    # 'age': [],
    'target': []
}

for path in [LT, TD]:
    for filename in fs.ls(path):
        raw = fs.open(filename, mode='r').read()
        if raw:
            transcript = json.loads(raw)['transcription']
        else:
            continue
        # Select the part of the file that matches the subpath in the CSV file
        subpath = filename.split('/')[-1]

        data['raw'].append(' '.join([utterance['text'] for utterance in transcript]))

        mini_df = process_children_data(transcript)
        data['numberofutterance'].append(mini_df.iloc[0, 0])
        data['avgWordsPerUtterance'].append(mini_df.iloc[0, 1])

        # data['age'].append(metadata.query('subpath == @subpath')['age'].iloc[0])
        data['target'].append('LT' if path == LT else 'TD')

df = pd.DataFrame(data)
train, test = train_test_split(df, test_size=0.3, random_state=10, stratify=df['target'])

train.to_csv('training_set.csv')
test.to_csv('test_set.csv')
