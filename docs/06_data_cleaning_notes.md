# Step 6: Data Cleaning Notes

## Actions Taken
We created a reusable Python module (`data_processing_05.py`) containing a `load_and_clean_data()` function. 

## Cleaning Steps Implemented
1. **Type Conversion:** Forced `TotalCharges` from string to numeric using `pd.to_numeric(..., errors='coerce')`. This correctly turned the empty spaces `" "` into standard `NaN` values.
2. **Imputation:** Filled the 11 `NaN` values in `TotalCharges` with `0`, because we identified logically that these were brand new customers (tenure = 0) who had not incurred any total charges yet.

## Engineering Lesson
Data cleaning should not be a loose script in a Jupyter Notebook. It should be wrapped in a reusable function so that the exact same cleaning logic can be applied to future/production data without copy-pasting code.
