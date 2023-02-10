import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def clean_webscrape_talkbank_transcription(csv_file_path, save_file_name):
    # read in the csv file as a df
    df = pd.read_csv(csv_file_path, delim_whitespace=True, header=None)

    # remove unimportant columns from the df
    useless_columns = [1, 3, 4, 6]
    for col in useless_columns:
        df.pop(col)

    # rename the columns
    df.columns = ['path_to_transcript', 'language', 'transcript_PID', 'activity_type', 'group_type']

    # include english only
    df = df[df['language'] == 'eng']

    # initialize a new column for the transcription
    df['transcription'] = ""

    # add transcription to each observation
    for i, row in df.iterrows():
        path = row.path_to_transcript
        # get web page
        url = "https://sla.talkbank.org/TBB/" + path + ".cha"

        ############### Begin Selenium
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(5)
        page = driver.page_source
        driver.quit()
        ############### End of Selenium

        soup = BeautifulSoup(page, 'html.parser')

        utt_list = []
        for utterance in soup.findAll(class_="utterance"):
            if utterance.span.strong.get_text(strip=True) == 'CHI:':
                utt_list.append(utterance.span.get_text(strip=False))

        df['transcription'].loc[i] = utt_list

    print(df['transcription'])
    df.to_csv(save_file_name)

