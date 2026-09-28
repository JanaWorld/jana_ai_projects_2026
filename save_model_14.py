import joblib
from split_and_train_08 import prepare_data
from tune_and_models_11 import build_advanced_pipeline

def save_winning_model():
    print("Loading and preparing data...")
    X_train, X_test, y_train, y_test = prepare_data()
    
    print("Building the winning pipeline (Balanced Logistic Regression)...")
    # We choose the model that won our Experiment 2
    pipeline = build_advanced_pipeline(model_type='logistic_balanced')
    
    print("Training the model on the training data...")
    pipeline.fit(X_train, y_train)
    
    print("Saving the model to 'churn_model.joblib'...")
    # joblib.dump saves the entire pipeline (including the Scaler and OneHotEncoder!)
    joblib.dump(pipeline, 'churn_model.joblib')
    
    print("✅ Model saved successfully! We are ready for Production.")

if __name__ == "__main__":
    save_winning_model()
