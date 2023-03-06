import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

  #open csv as dataframe
df = pd.read_csv('language_disorders_split_1.csv')
df  
df.describe()
#the input data (x, regressor)
x = np.array(df["0"]).reshape(-1,1)
x.shape
print(x)
#Lets try to find the output data (y, predictor)
y = np.array(df["6"])
y
y.shape
print(y)
print(type(y))
#split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=99)
#Exploring the train and test datasets
X_train.shape
X_test.shape
y.shape
print(y_train.shape)
print(y_test.shape)
