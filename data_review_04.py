import pandas as pd
import os
def review_data():
    # File paths
    excel_file = "telco_customer_churn.xlsx"

    
    # Load the dataset
    if os.path.exists(excel_file):
        print(f"Loading data from {excel_file}...")
        df = pd.read_excel(excel_file)
    else:
        print("Error: Could not find the dataset. Please make sure the file is in the 'churn' folder.")
        return
    # 1. Shape of the dataframe
    print("\n--- 1. DATASET SHAPE ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    # 2. DataFrame Info (datatypes and non-null counts)
    print("\n--- 2. DATATYPES & INFO ---")
    df.info()
    # 3. Missing Values
    print("\n--- 3. MISSING VALUES ---")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    if missing.sum() == 0:
        print("No missing values detected initially (but watch out for hidden ones like ' '!).")
    # 4. Summary Statistics for Numerical Columns
    print("\n--- 4. NUMERICAL STATISTICS ---")
    print(df.describe())
    print(df.head())
review_data()