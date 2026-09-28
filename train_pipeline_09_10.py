import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from split_and_train_08 import prepare_data

def build_model_pipeline():
    """
    Builds a complete Machine Learning Pipeline.
    """
    # 1. Identify which columns are numerical and which are categorical
    # We drop customerID earlier, and Churn is our 'y', so what's left is 'X'
    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    
    # Categorical features are everything else (gender, Contract, InternetService, etc.)
    # We can programmatically get them by asking pandas for 'object' types (strings)
    categorical_features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
        'Contract', 'PaperlessBilling', 'PaymentMethod'
    ]
    # Note: SeniorCitizen is currently an int64 (0/1), but it's technically a categorical feature. 
    # For now, treating it as categorical via OneHotEncoding is safe.

    # 2. Create the Preprocessors
    # Numeric preprocessor scales numbers to be between -1 and 1 (helps models learn)
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    # Categorical preprocessor converts words into numbers (One-Hot Encoding)
    # handle_unknown='ignore' prevents crashes if the model sees a new category in the future
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # 3. Combine Preprocessors into a ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 4. Create the final Pipeline with a Baseline Model (Logistic Regression)
    # Step 9 Model Selection: We always start with a simple model (Logistic Regression) 
    # before trying complex models like XGBoost.
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    
    return pipeline

if __name__ == "__main__":
    # 1. Get the data
    X_train, X_test, y_train, y_test = prepare_data()
    
    # 2. Get the pipeline
    model_pipeline = build_model_pipeline()
    
    print("\nTraining the Logistic Regression Baseline Model...")
    # 3. TRAIN the model. The pipeline automatically scales and encodes the training data!
    model_pipeline.fit(X_train, y_train)
    
    print("Evaluating the model on Test Data...")
    # 4. PREDICT on test data. The pipeline automatically applies the exact same scaling to test data!
    predictions = model_pipeline.predict(X_test)
    
    # 5. Step 12: Evaluation
    print("\n--- CONFUSION MATRIX ---")
    print(confusion_matrix(y_test, predictions))
    
    print("\n--- CLASSIFICATION REPORT ---")
    print(classification_report(y_test, predictions))
