# Step 13: Model Metrics Comparison

The following table summarizes the performance of our three experiments. Because our business objective is to catch as many churning customers as possible (minimizing False Negatives), our primary metric is **Recall (Class 1)**.

| Model Type | Recall (Churn) | Precision (Churn) | F1-Score (Churn) | Overall Accuracy | Missed Churners (False Negatives) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Baseline/Imbalanced)** | 0.56 | **0.66** | 0.60 | **0.81** | 165 |
| **Logistic Regression (Class Weight: Balanced)** | **0.78** | 0.50 | **0.61** | 0.74 | **81** |
| **Random Forest (Class Weight: Balanced)** | 0.62 | 0.55 | 0.58 | 0.77 | 143 |

## Business Conclusion
* **Accuracy is misleading:** The Baseline model had the highest overall accuracy (81%), but it was the worst at predicting our actual target (losing 165 customers).
* **The Trade-off:** By switching to a balanced Logistic Regression, we sacrificed Precision (dropping from 0.66 to 0.50), meaning we will accidentally give discounts to more loyal customers (False Positives). However, we vastly improved Recall (0.56 to 0.78), effectively saving 84 more high-risk customers from leaving.
* **Algorithm Complexity:** The Random Forest algorithm, while more complex, did not outperform the simpler Logistic Regression for this specific dataset and feature set. 
