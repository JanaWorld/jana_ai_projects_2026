# Step 8: Data Splitting Notes

## Actions Taken
We built `split_and_train_08.py` to prepare the data for the machine learning algorithms.

## Steps Implemented
1. **Drop Irrelevant Features:** Dropped the `customerID` column. Unique identifiers have no predictive power and will only confuse the ML model.
2. **Target Encoding:** Mapped the `Churn` column from "Yes"/"No" to `1`/`0`.
3. **Train/Test Split:** Split the dataset into 80% Training Data and 20% Testing Data.
4. **Stratification:** Used `stratify=y` to ensure that the 73/27 class imbalance between "Stay" and "Churn" was perfectly preserved in both the training and testing sets.

## Engineering Lesson (Data Leakage)
We split the data **before** doing any scaling or one-hot encoding. If you scale the entire dataset at once, the math uses the "future" test data to scale the training data. Splitting first guarantees zero data leakage.
