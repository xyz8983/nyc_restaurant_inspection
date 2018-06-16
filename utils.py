import pandas as pd
# import numpy as np
# import matplotlib
#
data_file = './data/NYC_Restaurant_Inspection_Results.csv'
#
def clean_data():

    inspection_raw = pd.read_csv(data_file)
    print(inspection_raw.head())

    return inspection_raw
