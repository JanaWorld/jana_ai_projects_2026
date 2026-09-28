# Step 4: Data Review Notes

## Actions Taken
We ran a Python script to inspect the raw `telco_customer_churn.xlsx` dataset using Pandas. 

## Key Discoveries
1. **Shape:** The dataset contains 7,043 rows and 23 columns.
2. **Missing Values Trap:** Pandas initially reported 0 missing values. However, upon inspecting the datatypes, we noticed `TotalCharges` was listed as an `object` (string) instead of a `float64`.
3. **The Hidden NaNs:** We discovered that 11 customers had an empty space `" "` in the `TotalCharges` column because their `tenure` was 0 (they were brand new customers who hadn't been billed yet). This forced the entire column to be treated as a string.

## Engineering Lesson
Never trust `df.isnull().sum()` blindly. Always check `df.info()` to ensure numerical columns are actually parsed as numbers. If a numerical column is an object, there is usually dirty data hiding inside it.
