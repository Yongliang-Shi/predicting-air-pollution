# Import libraries
import numpy as np
import pandas as pd
import os

def get_train_data():
    '''
    This function loads the train data into pandas dataframe.
    '''
    filename = "train.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print("Please download the data from Kaggle Compeition: Playground Prediction Competition")

def get_test_data():
    '''
    This function loads the test data into pandas dataframe.
    '''
    filename = "test.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print("Please download the data from Kaggle Compeition: Playground Prediction Competition")

def wrangle_train_data():
    '''
    This function prepare the train data for exploration and visualization.
    '''
    # Acuqire the training data
    df = get_train_data()

    # Rename the columns using a mapper
    col_names = {'date_time': 'datetime',
             'deg_C': 'temp',
             'target_carbon_monoxide': 'carbon_monoxide',
             'target_benzene': 'benzene',
             'target_nitrogen_oxides': 'nitrogen_oxides'}
    df = df.rename(columns=col_names)
    
    # Convert the values of the datetime column to the datetime64 dtype
    df.datetime = pd.to_datetime(df.datetime)

    # Split the values of the datetime column to date, time, day, month, year and weekday
    df = df.assign(
        date = [dt.date() for dt in df.datetime],
        time = [dt.time() for dt in df.datetime],
        day = [dt.day for dt in df.datetime],
        month = [dt.month for dt in df.datetime],
        year = [dt.year for dt in df.datetime],
        weekday = [dt.weekday() for dt in df.datetime]
    )

    # Set the datetime column as the index
    df = df.set_index('datetime')

    return df

def wrangle_test_data():
    '''
    This function prepare the test data for exploration and visualization.
    '''
    # Acuqire the test data
    df = get_test_data()

    # Rename the columns using a mapper
    col_names = {'date_time': 'datetime',
             'deg_C': 'temp',
             'target_carbon_monoxide': 'carbon_monoxide',
             'target_benzene': 'benzene',
             'target_nitrogen_oxides': 'nitrogen_oxides'}
    df = df.rename(columns=col_names)
    
    # Convert the values of the datetime column to the datetime64 dtype
    df.datetime = pd.to_datetime(df.datetime)

    # Split the values of the datetime column to date, time, day, month, year and weekday
    df = df.assign(
        date = [dt.date() for dt in df.datetime],
        time = [dt.time() for dt in df.datetime],
        day = [dt.day for dt in df.datetime],
        month = [dt.month for dt in df.datetime],
        year = [dt.year for dt in df.datetime],
        weekday = [dt.weekday() for dt in df.datetime]
    )

    # Set the datetime column as the index
    df = df.set_index('datetime')

    return df