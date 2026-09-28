# Customer Churn Prediction - Problem Definition

## 1. Business Context

**Who is the customer?**
Our customers are subscribers of a telecommunications company (e.g., internet, phone, and cable TV services).

**What does "churn" mean?**
Churn means that a customer has cancelled their subscription or ported their service to a competitor.

**Why does the company care?**
Acquiring new customers is generally 5 to 25 times more expensive than retaining existing ones. High churn directly leads to significant revenue loss.

**What happens if a customer churns?**
The company loses recurring monthly revenue from that customer and the marketing investment spent to acquire them.

**What decision will the prediction support?**
The prediction will help the retention team proactively identify at-risk customers and offer targeted interventions (like discounts or free upgrades) *before* they leave.

---

## 2. ML Framing

**Input:** 
Customer demographic information, account details, active services, billing history, and usage statistics.

**Output:** 
A binary label indicating whether the customer will churn (1 = Yes, 0 = No).

**Prediction Statement:** 
Given a customer's demographic, account, and usage information at the end of the current billing cycle, predict whether the customer will cancel their services within the next 30 days.

**Prediction timeframe:** 
The next 30 days.

**Business action:** 
Automatically trigger a personalized retention campaign (e.g., send an email with a 20% discount offer for a 6-month contract extension) for customers flagged as high-risk.

---

## 3. Senior-Engineer Questions (Preventing Data Leakage)

**When would the prediction be made?**
At the end of each customer's monthly billing cycle.

**What information would be available at prediction time?**
- Customer demographics
- Total tenure with the company
- Current active services
- Billing and payment history up to the current date
- Past support tickets or complaints

**What information would NOT be available?**
- Whether they have called to cancel *in the future* (next month).
- Usage statistics for the upcoming month.
- The actual churn date.
*(Including any of this in our training data would cause data leakage—the model would cheat by knowing the future).*
