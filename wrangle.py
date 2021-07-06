# Import libraries
import numpy as np
import pandas as pd
import os

def get_training_data():
    '''
    This function loads the training data
    '''
    filename = "train.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print("Please download the data from Kaggle Compeition: Playground Prediction Competition")

def wrangle_training_data():
    '''
    This function prepare the training data for exploration and visualization.
    '''
    # Acuqire the training data
    df = get_training_data()

    # Rename the columns using a mapper
    col_names = {'date_time': 'datetime',
             'deg_C': 'temp',
             'target_carbon_monoxide': 'carbon_monoxide',
             'target_benzene': 'benzene',
             'target_nitrogen_oxides': 'nitrogen_oxides'}
    df = df.rename(columns=col_names)
    
    # Correct the datatype of the datetime column
    df.datetime = pd.to_datetime(df.datetime)

    # Split the datetime column to separate date and time
    df = df.assign(date = [dt.date() for dt in df.datetime], 
                time = [dt.time() for dt in df.datetime])

    # Split the date into day, month, and year
    df = df.assign(day=[d.day for d in df.date], 
                month = [d.month for d in df.date],
                year = [d.year for d in df.date])

    # Set the datetime column as the index
    df = df.set_index('datetime')

    return df