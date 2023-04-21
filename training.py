import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('training_set.csv')

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    max_features='sqrt',
    max_leaf_nodes=None,
)

model.fit(train[['numberofutterance','avgWordsPerUtterance']], train['target'])

pickle.dump(model, open('rf_model1.pickle', 'wb'))