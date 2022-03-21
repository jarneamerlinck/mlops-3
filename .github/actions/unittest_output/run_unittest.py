# Simple unit test for checking that all wanted columns are in our raw data
import pandas as pd

def unittest_output_predictions(df: pd.DataFrame, outcome_var_name:str, accepted_values: list=[0,1]):
    """Test whether output values are within the accepted list of values

    Args:
        df (pd.DataFrame): dataframe with predictions
        outcome_var_name (str): name of outcome variable
        accepted_values (list, optional): list of accepted values. Defaults to [0,1].
    """
    predicted_values = df[outcome_var_name]
    
    for row, val in enumerate(predicted_values):
        assert val in accepted_values, f'Value {val} at row {row} is not an accepted prediction'

def main():
    # Read data
    predictions = pd.read_csv('data/output/final_predictions.csv')
    
    # Unit tests
    unittest_output_predictions(predictions, 'Survived', [0,1])
    
    # Success
    print('All output unit tests passed!')
    
if __name__ == '__main__':
    main()