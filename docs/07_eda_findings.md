# EDA Findings & ML Relevance

After generating the visualizations, here is the story the data tells us about why customers are leaving, and how our Machine Learning model will use this information.

### 1. Target Variable Distribution (`01_churn_distribution`)
* **Observation:** The dataset is imbalanced. There are many more people who stay ("No") than people who leave ("Yes"). The ratio is roughly 73% No to 27% Yes.
* **ML Relevance:** Because the data is imbalanced, an ML model could just guess "No" every time and be 73% accurate. This confirms why we chose **Recall** as our metric in Step 2, instead of Accuracy.

### 2. Numerical Distributions (`02_numerical_distributions`)
* **Tenure (Months with company):**
  * **Observation:** The highest churn happens in the first 1-5 months. If a customer stays for 2+ years, they almost never leave.
  * **Business Action:** The company needs a better "onboarding" or 90-day retention program.
* **Monthly Charges:**
  * **Observation:** As we saw in our python script, higher monthly charges mean much higher churn. Cheap plans (around $20/month) have almost zero churn.

### 3. Contract Type vs Churn (`03_contract_vs_churn`)
* **Observation:** Customers on **Month-to-month** contracts are churning at an alarming rate. Customers locked into 1-year or 2-year contracts rarely leave.
* **ML Relevance:** The `Contract` column will be one of the strongest predictive features for our model.

### 4. Internet Service vs Churn (`04_internet_vs_churn`)
* **Observation:** Customers with **Fiber optic** internet have a massive churn rate compared to DSL. 
* **Business Action:** This is a red flag! Fiber optic is usually the premium product. The business needs to investigate if the Fiber service is dropping out, if the customer service for it is bad, or if a competitor is undercutting their Fiber prices.

---
**Summary:** A high-risk customer looks like this: A brand new customer (low tenure), on a month-to-month contract, paying a high monthly bill for Fiber Optic internet.
