import pandas as pd
import numpy as np
import os

datadir = '/home/ubuntu/environment/speech-language-screening/data/raw_talkbank_data'
rawdata_file = os.path.join(datadir, 'language_disorders.csv')


print(rawdata_file)

#Read the data file
df = pd.read_csv(rawdata_file )

#drop the first two column as its redundant 
df.drop(df.columns[[0,1]], axis=1, inplace=True)

#shuffle the data
df = df.sample(frac=1).reset_index(drop=True)


# split data into train, test and validation sets with 60%, 20% and 20% of the data respectively and save them to separate csv files
train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
trainFile = os.path.join(datadir, 'train.csv')
train.to_csv(trainFile, index=False)

validateFile =  os.path.join(datadir, 'validate.csv')
validate.to_csv(validateFile, index=False)

testFile = os.path.join(datadir, 'test.csv')
test.to_csv(testFile, index=False)

# Read the train, test and validation data files and print the shape of each
train = pd.read_csv(trainFile)
validate = pd.read_csv(validateFile)
test = pd.read_csv(testFile)
print(f"The shape of the train data is {train.shape}")
print(f"The shape of the validate data is {validate.shape}")
print(f"The shape of the test data is {test.shape}")

