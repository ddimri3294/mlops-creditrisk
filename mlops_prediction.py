import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


@st.cache(allow_output_mutation=True)
def load_model():
    pickled_model = joblib.load('/mlops/models/lgb.pkl')
    return pickled_model


def explore(data):
    # DATA
    st.write('Data with Predicted Output:')

    with st.spinner("loading model into memory........."):
        pickled_model = load_model()

    with st.spinner("calculating probability........."):
        for iter, row in data.iterrows():
            X_test = list(row)

            X_test = np.array(X_test)
            X_test = np.expand_dims(X_test, axis=0)

            pred = pickled_model.predict_proba(X_test)[0]

            if iter == 0:
                data["predicted_probability"] = max(pred)
            else:
                data.at[iter, "predicted_probability"] = max(pred)

    st.write(data)


def get_df(file):
    # get extension and read file
    df = pd.DataFrame()

    extension = file.name.split('.')[-1]
    if extension.upper() == 'CSV':
        df = pd.read_csv(file)

    return df


def main():
    st.title('Class Probability')
    st.write('Credit risk exploratory app')
    file = st.file_uploader("Upload file", type=['csv'])
    try:
        dataframe = get_df(file)
        explore(dataframe)
    except Exception as e:
        st.write(f"{str(e)}")


if __name__ == "__main__":
    main()
