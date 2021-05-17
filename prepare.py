### Prepare Data Function File ###
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



################################ Prepare Iris Data Function ############################
def prep_iris():
    '''
    This function loads the untransformed iris data and returns the data with dropped
    redundant columns and dummy variables (preparing the data)
    '''
    df = get_iris_data()
    df = df.drop(columns='species_id').rename(columns={'species_name': 'species'})
    species_dummies = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df, species_dummies], axis=1)
    
    return df


################################ Prepare/Split Data Function ############################


def titanic_split(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on survived.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.survived)
    return train, validate, test

############################ Clean Titanic Data ############################

def clean_data(df):
    '''
    This function will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'], fill missing embark_town with 'Southampton'
    and create dummy vars from sex and embark_town. 
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['deck', 'embarked', 'class', 'age'])
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df

########################### Prep Titanic Data ##############################

def prep_titanic_data(df):
    '''
    This function takes in a df and will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'], fill missing embark_town with 'Southampton'
    create dummy vars from sex and embark_town, and perform a train, validate, test split. 
    Returns train, validate, and test DataFrames
    '''
    df = clean_data(df)
    train, validate, test = titanic_split(df)
    return train, validate, test


 