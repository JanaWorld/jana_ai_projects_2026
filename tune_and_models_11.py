import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from split_and_train_08 import prepare_data

def build_advanced_pipeline(model_type='logistic_balanced'):
    """
    Builds a pipeline with different model options.
    """
    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    categorical_features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
        'Contract', 'PaperlessBilling', 'PaymentMethod'
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline(steps=[('scaler', StandardScaler())]), numeric_features),
            ('cat', Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))]), categorical_features)
        ])

    # Choose the model based on the argument
    if model_type == 'logistic_balanced':
        # class_weight='balanced' forces the model to pay more attention to the minority class (Churn=1)
        classifier = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    elif model_type == 'random_forest':
        # A more complex tree-based model
        classifier = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', classifier)
    ])
    
    return pipeline

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data()
    
    for model_name in ['logistic_balanced', 'random_forest']:
        print(f"\n{'='*40}")
        print(f"Training Model: {model_name}")
        print(f"{'='*40}")
        
        pipeline = build_advanced_pipeline(model_type=model_name)
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)
        
        print("\n--- CONFUSION MATRIX ---")
        print(confusion_matrix(y_test, predictions))
        
        print("\n--- CLASSIFICATION REPORT ---")
        print(classification_report(y_test, predictions))
