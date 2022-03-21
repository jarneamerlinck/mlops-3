# Load packages
## Data wrangling
import pandas as pd

## Model saving
import pickle

# Main function to use trained model to make predictions on our testing data
def main():
    # Read preprocessed testing data
    test = pd.read_csv('data/preprocessed/test_preprocessed.csv')
    X_test = test.drop('PassengerId', axis=1) # The PassengerId feature is not used for predicting, so we need to remove this
    
    # Load our trained model
    model_filename = 'models/trained_model.pkl'
    
    with open(model_filename, 'rb') as file:
        trained_model = pickle.load(file)
    
    # Create predictions
    predictions = trained_model.predict(X_test)
    
    # Reformat into dataframe
    final_predictions = pd.DataFrame([test.PassengerId, predictions]).T
    final_predictions.columns = ['PassengerId','Survived']
    
    # Print results
    print('Sample of predictions: ')
    print(final_predictions.head())
    
    # Save our predictions as csv
    final_predictions.to_csv('data/output/final_predictions.csv',index=False)
    
if __name__=='__main__':
    main()