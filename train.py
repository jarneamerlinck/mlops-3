# Load packages
## Data wrangling
import pandas as pd
import numpy as np

## Model training
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

## Model saving
import pickle

# Main function for training model on split train data and evaluating on validation data
def main():
    # Read preprocessed training data
    train = pd.read_csv('data/preprocessed/train_preprocessed.csv')
    
    # Seperate our features from our outcome variable
    X_full = train.drop('Survived', axis=1)
    y_full = train.Survived
    
    # Split our non-test set into a training and validation set
    X_train, X_valid, y_train, y_valid = train_test_split(X_full, y_full, test_size=0.3, random_state=0)
    
    # Train a RandomForestClassifier
    model = RandomForestClassifier(n_estimators=20, random_state=0)
    print(f'Training {model}')
    model.fit(X_train, y_train)
    
    # Make prediction on our validation dataset
    predict = model.predict(X_valid)
    
    # Show our model accuracy on the validation data
    accuracy = metrics.accuracy_score(y_valid, predict)
    print('Valid Accuracy: ',np.round(accuracy, 4))
    
    # Train model on the full dataset
    model.fit(X_full, y_full)
    
    # Save our model weights and parameters to a pickle file
    model_name = 'models/trained_model.pkl'
    with open(model_name, 'wb') as file:
        pickle.dump(model, file)
    
if __name__=='__main__':
    main()