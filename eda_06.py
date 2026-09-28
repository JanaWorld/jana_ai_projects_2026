import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_processing_05 import load_and_clean_data

def run_eda():
    # Load clean data
    df = load_and_clean_data("telco_customer_churn.xlsx")
     # Let's do the EDA task on our clean dataframe!
    
    print("\n--- EDA: Average Monthly Charges by Churn ---")
    print(df.groupby('Churn')['MonthlyCharges'].mean())
    # Create an output directory for our plots
    os.makedirs("eda_plots", exist_ok=True)
    
    # Set seaborn style for prettier plots
    sns.set_theme(style="whitegrid")
    
    print("Generating EDA plots...")
    
    # 1. Target Variable Distribution (Class Imbalance)
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Churn', palette='Set2')
    plt.title('Target Variable Distribution (Churn)')
    plt.savefig('eda_plots/01_churn_distribution.png')
    plt.close()
    
    # 2. Numerical Features Distribution by Churn
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', ax=axes[0], palette='Set2')
    axes[0].set_title('Tenure Distribution by Churn')
    
    sns.histplot(data=df, x='MonthlyCharges', hue='Churn', multiple='stack', ax=axes[1], palette='Set2')
    axes[1].set_title('Monthly Charges Distribution by Churn')
    
    sns.histplot(data=df, x='TotalCharges', hue='Churn', multiple='stack', ax=axes[2], palette='Set2')
    axes[2].set_title('Total Charges Distribution by Churn')
    
    plt.tight_layout()
    plt.savefig('eda_plots/02_numerical_distributions.png')
    plt.close()
    
    # 3. Contract Type vs Churn (Important Business Metric)
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
    plt.title('Churn by Contract Type')
    plt.savefig('eda_plots/03_contract_vs_churn.png')
    plt.close()
    
    # 4. Internet Service vs Churn
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='InternetService', hue='Churn', palette='Set2')
    plt.title('Churn by Internet Service Type')
    plt.savefig('eda_plots/04_internet_vs_churn.png')
    plt.close()

    print("EDA plots successfully generated and saved in the 'eda_plots/' folder!")

if __name__ == "__main__":
    run_eda()
