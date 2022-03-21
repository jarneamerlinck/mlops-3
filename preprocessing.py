# Load packages
## Data wrangling
import pandas as pd
import numpy as np

## Helpers
from helpers.preprocessing_helpers import map_numeric, replace_na

# Main preprocessing function
def main():
    # Read data
    train = pd.read_csv('data/raw/train.csv')
    test = pd.read_csv('data/raw/test.csv')
    
    # Convert required categorical features to numeric features
    mapping_features = ['Sex','Embarked']
    mapping_dicts = [{'male':0, 'female':1}, {'S':0,'C':1,'Q':1}]
    
    for mapping_feature, mapping_dict in zip(mapping_features, mapping_dicts):
        train, test = map_numeric(train, test, mapping_feature, mapping_dict)
    
    # Replace NA with wanted values for features that have NAs
    na_features = ['Age','Embarked','Fare']
    na_values = [np.mean(train.Age), 0, np.mean(train.Fare)] # I'm lazy here...I'm using the train means to impute both the train and test data.
    
    for na_feature, na_value in zip(na_features, na_values):
        train, test = replace_na(train, test, na_feature, na_value)
    
    # Subset on features of interest
    train_features = ['Survived','Pclass','Sex','Age','SibSp','Parch','Embarked','Fare']
    test_features = ['PassengerId','Pclass','Sex','Age','SibSp','Parch','Embarked','Fare']
    
    train = train.loc[:,train_features]
    test = test.loc[:,test_features]

    # Inspect our result
    print('\nPreprocesssed Train: \n', train.head(3))
    print('\nPreprocesssed Test: \n', test.head(3))
    
    # Save results
    train.to_csv('data/preprocessed/train_preprocessed.csv',index=False)
    test.to_csv('data/preprocessed/test_preprocessed.csv',index=False)

if __name__ == '__main__':
    main()