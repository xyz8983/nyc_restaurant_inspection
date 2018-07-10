import pandas as pd
# import numpy as np
# import matplotlib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
#
data_file = './data/NYC_Restaurant_Inspection_Results.csv'
#
def clean_data():

    inspection_raw = pd.read_csv(data_file)
    print(inspection_raw.head())

    # clean the column 'Violation description', decode to remove special characters,
    # remove the stop words and punctuations
    for index, desc in inspection_raw['VIOLATION DESCRIPTION'].interitems():
        if desc:
            # tokennize it
            temp = word_tokenize(desc)
            # remove punctuation and stopwords
            temp = [w for w in temp if w not in stopwords.words('english') and w not in punctuation]

            inspection_raw['desc_token'][index] = temp

        else:
            inspection_raw['desc_token'][index] = ''
            # give it an empty string. word_tokenize will return error if the param is None


    return inspection_raw
