import pandas as pd
import joblib
import numpy as np
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

df = pd.read_csv("Sample_input_variables.csv")
probs = []
for iter, row in df.iterrows():
    X_test = list(row)

    X_test = np.array(X_test)
    X_test = np.expand_dims(X_test, axis=0)

    pickled_model = joblib.load('models/lgb.pkl')
    pred = pickled_model.predict_proba(X_test)[0]

    pred = max(pred)
    probs.append(pred)

# Write scores to a file
with open("metrics.txt", 'w') as outfile:
    for pred in probs:
        outfile.write("probability result: %2.1f\n" % pred)

