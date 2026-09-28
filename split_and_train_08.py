import pandas as pd
from sklearn.model_selection import train_test_split
from data_processing_05 import load_and_clean_data

def prepare_data(filepath="telco_customer_churn.xlsx"):
    """
    Loads clean data, drops irrelevant columns, and splits into Train and Test sets.
    Returns X_train, X_test, y_train, y_test
    """
    # 1. Load clean data
    df = load_and_clean_data(filepath)
    
    # 2. Drop columns that have no predictive power
    # customerID is just a random string, it doesn't help predict churn!
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)
        
    # 3. Separate Features (X) from Target (y)
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    # 4. Encode the Target variable from 'Yes'/'No' to 1/0
    # Machine Learning models need numbers, not strings.
    y = y.map({'Yes': 1, 'No': 0})
    
    # 5. Split the data!
    # test_size=0.2 means 20% of data is saved for testing.
    # random_state ensures we get the exact same split every time we run the script.
    # stratify=y ensures the 73/27 class imbalance is maintained in both train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    print("Preparing and splitting data...")
    X_train, X_test, y_train, y_test = prepare_data()
    
    print("\n--- SPLIT RESULTS ---")
    print(f"Training Data (X_train): {X_train.shape[0]} rows, {X_train.shape[1]} features")
    print(f"Testing Data (X_test):   {X_test.shape[0]} rows, {X_test.shape[1]} features")
    print(f"Target Train (y_train):  {y_train.shape[0]} rows")
    print(f"Target Test (y_test):    {y_test.shape[0]} rows")
    
    print("\nNext step: We will build a Scikit-Learn Pipeline to encode these features and train a model!")
