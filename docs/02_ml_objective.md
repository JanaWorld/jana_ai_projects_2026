# Step 2: ML Objective Definition

## 1. Problem Formulation
**Problem Type:** Binary Classification
*(We are classifying customers into one of two groups: they will churn or they will not).*

**Target Variable:** `churn_status` (or simply `churn`)

**Positive Class (1):** Customer churns (cancels service).
**Negative Class (0):** Customer stays (retained).

---

## 2. Metric Selection & Business Cost Analysis

In ML, accuracy is often a bad metric, especially if classes are imbalanced (e.g., if only 5% of customers churn, a model that predicts "Nobody churns" is 95% accurate, but 100% useless).

We need to evaluate the cost of errors:

* **False Positive (FP):** The model predicts the customer will churn, but they were actually going to stay.
  * **Business Cost:** We spend money giving a discount/promotion to someone who didn't need it. We lose some margin, but we keep the customer.
  
* **False Negative (FN):** The model predicts the customer will stay, but they actually churn.
  * **Business Cost:** We do nothing, and the customer leaves. We lose their entire recurring revenue and must spend a lot to acquire a replacement.

**Conclusion on Errors:**
In customer churn, a **False Negative is usually much more expensive than a False Positive**. It is better to accidentally give a discount to a loyal customer than to let a high-value customer slip away without intervention.

### Our Chosen Metrics:
* **Primary Metric:** **Recall** (Sensitivity) for the positive class. We want to identify as many actual churners as possible, minimizing False Negatives.
* **Secondary Metrics:** 
  * **F1-Score:** To ensure we don't completely sacrifice Precision (giving discounts to *everyone* is too expensive).
  * **ROC-AUC:** To evaluate the model's overall ability to separate churners from non-churners across different thresholds.
