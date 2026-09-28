# Step 3: Data Collection

## Dataset Overview
* **Dataset Name:** IBM Telco Customer Churn Dataset
* **Source:** IBM / Kaggle
* **Number of Rows:** 7,032
* **Number of Columns:** 23
* **Target Column:** `Churn` (Yes/No)
* **Data Format:** CSV / Excel

## Data Collection Assumptions & Real-World Mindset
While we are using a static CSV file for this training project, in a real-world company, this data would not exist in one single file. It would be pieced together from multiple systems:

1. **CRM / User Database:** `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`
2. **Billing System:** `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`, `tenure`
3. **Application/Service Logs:** `PhoneService`, `InternetService`, `OnlineSecurity`, `TechSupport`, `StreamingTV`, etc.
4. **Customer Support System (Zendesk, etc.):** `numAdminTickets`, `numTechTickets`

In production, a Data Engineer would build a pipeline (e.g., using SQL or Spark) to join these tables together into a "Feature Store" or a final view that our ML model can query.

## Potential Issues to Watch Out For
* Are the `TotalCharges` dynamically updated, or is it a snapshot in time? 
* `numAdminTickets` and `numTechTickets` might be highly correlated with churn—we must ensure they are counted *up to* the prediction date, not after the customer already decided to leave.
