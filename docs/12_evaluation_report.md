# Step 12: Model Evaluation Report

## Experiment 1: Baseline Logistic Regression (No class weighting)
**Model Type:** `LogisticRegression(max_iter=1000)`

### Confusion Matrix
```
[[926 109]
 [165 209]]
```
* **True Positives:** 209
* **False Negatives:** 165 (Missed churners)
* **Recall (Class 1):** 0.56 (56%)
* **Overall Accuracy:** 81%

### Business Analysis of Experiment 1
With a recall of 0.56, the model is entirely missing 44% (165 out of 374) of our churning customers. This is caused by the class imbalance in the training data (73% non-churners vs 27% churners).

---

## Experiment 2: Tuned Logistic Regression
**Model Type:** `LogisticRegression(class_weight='balanced')`

### Confusion Matrix
```
[[747 288]
 [ 81 293]]
```
* **True Positives:** 293
* **False Negatives:** 81 (Missed churners)
* **Recall (Class 1):** 0.78 (78%)
* **Overall Accuracy:** 74%

### Business Analysis of Experiment 2
This is a massive success! By adding a single mathematical penalty (`class_weight='balanced'`), our Recall skyrocketed from 56% to 78%. 
* Baseline Model: Missed 165 churning customers.
* Tuned Model: Missed only 81 churning customers.
We effectively cut the business losses in half. Notice that our overall Accuracy *dropped* from 81% to 74% (because we are making more False Positive errors now, predicting "Yes" more often), but in the context of Churn, losing 81 customers is far cheaper than losing 165 customers.

---

## Experiment 3: Random Forest
**Model Type:** `RandomForestClassifier(class_weight='balanced')`

### Confusion Matrix
```
[[847 188]
 [143 231]]
```
* **True Positives:** 231
* **False Negatives:** 143 (Missed churners)
* **Recall (Class 1):** 0.62 (62%)
* **Overall Accuracy:** 77%

### Business Analysis of Experiment 3
Despite being a more "complex" and theoretically powerful model, the Random Forest performed much worse than our simple Logistic Regression on our primary metric (Recall 62% vs 78%). It missed 143 churners. This is why ML Engineers test baselines—complex doesn't always mean better for the specific business metric.

**WINNER:** Experiment 2 (`LogisticRegression(class_weight='balanced')`)
