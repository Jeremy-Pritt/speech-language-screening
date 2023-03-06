import numpy as np
import pandas as pd
from datetime import datetime
# import nltk as nltk

df = pd.read_csv("/home/ubuntu/environment/speech-language-screening/data/raw_talkbank_data/clean.py")

df.head()

df.loc[:, [ 'age', 'sex', 'group_type', 'transcription']]

df.loc[df["group_type"] == "LT", "group_type"] = "SLI"


ages = []
for i in df['age']:
  str(i)
  ages.append(i)
  
for j in ages:
  year_month = j.rsplit('.')[0]
  year = year_month[0]
  month = year_month[2]