import requests
from io import BytesIO
import pandas as pd
import numpy as np
from pydub import AudioSegment
from process_audio_webscrape import process_audio_webscrape
import time


def scrape_audio_TB(url):
    response = requests.get(url)

    with open(r'temp_audio.mp3', 'wb') as f:
        f.write(response.content)

    samples, sampling_rate = process_audio_webscrape(r'temp_audio.mp3')
    return samples, sampling_rate


# url = r"https://media.talkbank.org/childes/Clinical-MOR/ENNI/SLI/413"
# print(scrape_audio_TB(url))

def get_TB_audio(csv_file_path, save_file_name):
    """
    webscrapes TalkBank audio data
    :param csv_file_path: csv file from TalkBankDB with transcription pages metadata
    :param save_file_name: file path to the location the outputted csv file will be saved to
    :return: csv file with webscraped audio data for each transcription page in input csv file
    """
    # read in the csv file as a df
    df = pd.read_csv(csv_file_path, delim_whitespace=True,
                     header=None)

    df = df.sample(frac=1, random_state=55).iloc[500:700, :]

    # remove unimportant columns from the df

    useless_columns = [3, 4, 5, 6]
    for col in useless_columns:
        df.pop(col)

    # rename the columns
    df.columns = ['path_to_transcript', 'subject_id', 'language', 'sample_type',
                  'group_type']

    # initialize new columns
    df['samples'] = ""
    df['sampling_rate'] = ""

    # loop through each transcription webpage in the dataframe
    for i, row in df.iterrows():
        try:
            path = row.path_to_transcript

            url = "https://media.talkbank.org/" + path

            samples, sr = scrape_audio_TB(url)

            # update dataframes with extracted data
            df['samples'].loc[i] = samples
            df['sampling_rate'].loc[i] = sr

        except:
            print("skipped at this index:", i)
            continue

    # save to the specified file path, save_file_name
    df.to_csv(save_file_name)


# call
get_TB_audio(r"data/talkbank_transcripts_metadata/audio_langdisorders_metadata.csv",
             r"data/raw_talkbank_data/audio_language_disorders_scraped_6.csv")
