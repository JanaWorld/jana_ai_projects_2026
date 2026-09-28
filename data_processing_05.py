import pandas as pd
import os

def load_and_clean_data(filepath):
    """
    Loads the dataset and performs all necessary data cleaning steps.
    Returns a clean pandas DataFrame ready for Feature Engineering / ML.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Cannot find data file at {filepath}")
        
    print(f"Loading data from {filepath}...")
    if filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        df = pd.read_csv(filepath)
        
    # --- CLEANING STEP 1: Fix TotalCharges ---
    # Convert 'TotalCharges' to numeric, forcing errors/blank spaces to NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Fill the resulting NaNs with 0 (since they are new customers with 0 tenure)
    df['TotalCharges'] = df['TotalCharges'].fillna(0)
    
    # (Future cleaning steps like handling outliers or dropping useless columns like customerID will go here)
    print("Data cleaning complete!")
    
    return df

if __name__ == "__main__":
    # Test our cleaning function
    clean_df = load_and_clean_data("telco_customer_churn.xlsx")
    
   