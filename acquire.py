### Functions for use in classifications exercise

import pandas as pd
import numpy as np
import os
from env import host, user, password

#############################Connect To SQL database Function##############################

def sql_connect(db, user=user, host=host, password=password):
    '''
    This function allows me to connect the Codeup database to pull SQL tables
    Using private information from my env.py file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#############################Acquire Titanic Database Lightspeed###########################

def get_titanic_data():
    '''
    This function connects to Codeup database and read the passengers table from 
    the Titanic database into a pandas dataframe.
    '''
    sql_query = 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, sql_connect('titanic_db'))
    return df

##############################Acquire Iris Database Lightspeed#############################

def get_iris_data():
    '''
    This function reads the iris data and joins two tables then makes that into a dataframe
    '''
    sql_query = """
                SELECT species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species
                USING(species_id)
                """
    df = pd.read_sql(sql_query, sql_connect('iris_db'))
    return df

################################Acquire Titanic CSV Lightspeed###############################

def get_titanic_csv(cached=False):
    if cached == False or os.path.isfile('titanic_df.csv') == False:
        df = get_titanic_data()
        df.to_csv('titanic_df.csv')
    else:
        df = pd.read_csv('titanic_df.csv', index_col=0)
    return df

#################################Acquire Iris CSV Lightspeed#################################

def get_iris_csv(cached=False):
    if cached == False or os.path.isfile('iris_df.csv') == False:
        df = get_iris_data()
        df.to_csv('iris_df.csv')
    else:
        df = pd.read_csv('iris_df.csv', index_col=0)
    return df