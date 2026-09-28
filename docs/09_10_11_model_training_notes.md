# Steps 9, 10, & 11: Model Training and Tuning Notes

## Actions Taken
We built a professional Scikit-Learn **Pipeline** to handle feature encoding, scaling, and model training in one seamless step.

## Pipeline Architecture
1. **Numerical Transformer:** Applies `StandardScaler()` to `tenure`, `MonthlyCharges`, and `TotalCharges`.
2. **Categorical Transformer:** Applies `OneHotEncoder()` to all string-based columns (like Contract, InternetService, etc.) to turn them into binary flags.
3. **ColumnTransformer:** Combines the two transformers so they act simultaneously on the respective columns.

## Models Tested
* **Step 9 (Model Selection):** We started with a baseline `LogisticRegression` model. A good ML engineer always establishes a simple baseline before trying complex neural networks.
* **Step 11 (Hyperparameter Tuning):** Because our baseline missed 44% of churning customers (due to the 73/27 class imbalance), we tuned the model using the `class_weight='balanced'` hyperparameter. This forces the algorithm to penalize errors on the minority class (Churn) much more heavily. We also introduced a `RandomForestClassifier` to see if a tree-based architecture performs better.
