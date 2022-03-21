# Simple unit test for checking that all wanted columns are in our raw data
import pandas as pd

TRAIN_COLUMNS = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp' ,'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
TEST_COLUMNS = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

def unittest_input_cols(df: pd.DataFrame, cols: str, dataset_name: str):
    """Test whether columns in data match input columns

    Args:
        df (pd.DataFrame): train or test df
        cols (str): columns to check against
        dataset_name (str): name of dataset. Should be either 'train' or 'test'.
    """ 
    for col in df.columns:
        assert col in cols, f'{col} missing in {dataset_name} dataset'
    assert len(cols) == len(df.columns), f'More columns in {dataset_name} than expected'

def main():
    # Read data
    train = pd.read_csv('data/raw/train.csv')
    test = pd.read_csv('data/raw/test.csv')
    
    # Unit tests
    unittest_input_cols(train, TRAIN_COLUMNS, 'train')
    unittest_input_cols(test, TEST_COLUMNS, 'test')
    
    # Success
    print('All input unit tests passed!')
    
if __name__ == '__main__':
    main()
