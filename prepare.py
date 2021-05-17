### Prepare Data Function File ###

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