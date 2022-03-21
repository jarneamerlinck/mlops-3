import pandas as pd
from typing import Tuple # Module to help with type hinting

def map_numeric(train: pd.DataFrame, test: pd.DataFrame, feature: str, mapping: dict) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Map categorical features to numeric values for both train and test datasets

    Args:
        train (pd.DataFrame): training data
        test (pd.DataFrame): testing data
        feature (str): feature name
        mapping (dict): mapping dict in the format of {'feature_value':'new_value'}

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: (train, test)
    """
    for df in [train, test]:
        df[feature] = df[feature].map(mapping)
    
    return train, test

def replace_na(train: pd.DataFrame, test: pd.DataFrame, feature: str, replace_value: any) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Replace NAs of specified features with chosen values for both train and test

    Args:
        train (pd.DataFrame): training data
        test (pd.DataFrame): testing data
        feature (str): feature name
        replace_value (any): new values for NAs

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: (train, test)
    """
    for df in [train, test]:
        df[feature] = df[feature].fillna(replace_value)
    
    return train, test