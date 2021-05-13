### Functions for use in classifications exercise

import pandas as pd
import numpy as np
import os
from env import host, user, password

def sql_connect(db, user=user, host=host, password=password):
    '''
    This function allows me to connect the Codeup database to pull SQL tables
    Using private information from my env.py file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    This function connects to Codeup database and read the passengers table from 
    the Titanic database into a pandas dataframe.
    '''
    sql_query = 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, sql_connect('titanic_db'))
    return df

def new_iris_data():
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
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    return df