# Import libraries
import numpy as np
import pandas as pd
import os

def get_training_data():
    '''
    This function load the training data
    '''
    filename = "train.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print("Please download the data from Kaggle Compeition: Playground Prediction Competition")

