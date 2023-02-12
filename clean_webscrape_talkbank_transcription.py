import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def clean_webscrape_talkbank_transcription(csv_file_path, save_file_name):
    """
    webscrapes TalkBank transcription data
    :param csv_file_path: csv file from TalkBankDB with transcription pages metadata
    :param save_file_name: file path to the location the outputted csv file will be save to
    :return: csv file with webscraped transcription data for each transcription page in input csv file
    """
    # read in the csv file as a df
    df = pd.read_csv(csv_file_path)

    # remove unimportant columns from the df
    useless_columns = ["Unnamed: 0", "index", "1", "4", "5", "3"]
    for col in useless_columns:
        df.pop(col)

    # rename the columns
    df.columns = ['path_to_transcript', 'language', 'study_type', 'activity_type', 'group_type']

    # include english only
    df = df[df['language'] == 'eng']

    # initialize new columns
    df['age'] = ""
    df['sex'] = ""
    df['transcription'] = ""

    # loop through each transcription webpage in the dataframe
    for i, row in df.iterrows():
        try:

            path = row.path_to_transcript
            # get web page
            url = "https://sla.talkbank.org/TBB/" + path + ".cha"

            # open and read in the transcription webpage
            driver = webdriver.Firefox()
            driver.get(url)
            time.sleep(6)
            page = driver.page_source
            driver.quit()

            # parse the web page HTML
            soup = BeautifulSoup(page, 'html.parser')

            # extract transcription from soup
            utt_list = []
            for utterance in soup.findAll(class_="utterance"):
                if utterance.span.strong.get_text(strip=True) == 'CHI:':
                    utt_list.append(utterance.span.get_text(strip=False))

            # extract age and sex from soup
            age = ""
            sex = ""
            metaDataTable = soup.findAll(class_="metaDataTable")[1]
            for tr_tag in metaDataTable.find_all('tr')[1:]:
                if tr_tag.td.text == 'CHI':
                    age = tr_tag.select("td:nth-of-type(" + str(5) + ")")[0].text
                    sex = tr_tag.select("td:nth-of-type(" + str(6) + ")")[0].text

            # update dataframes with extracted data
            df['age'].loc[i] = age
            df['sex'].loc[i] = sex
            df['transcription'].loc[i] = utt_list

        except:
            print("skipped at this index:", i)
            continue

    # save to the specified file path, save_file_name
    df.to_csv(save_file_name)

# call
clean_webscrape_talkbank_transcription(r"TalkBank Transcripts MetaData/language_disorders_split_2.csv", r"Clean TalkBank Data/language_disorders_scraped_split_2.csv")