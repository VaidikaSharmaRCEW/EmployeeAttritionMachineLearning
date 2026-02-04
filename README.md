# 🧑‍💼 Employee Attrition Prediction using Machine Learning

## 📌 Project Overview
Employee attrition is a critical challenge for organizations as it affects productivity, cost, and team morale.  
This project aims to predict whether an employee is likely to leave the organization using Machine Learning techniques.

By analyzing employee demographic, job-related, and satisfaction data, the model helps HR teams take proactive retention measures.

---

## 📊 Dataset Details
- **Dataset Name:** IBM HR Analytics Employee Attrition Dataset  
- **Source:** Kaggle  
- **File Format:** CSV  
- **Target Variable:** Attrition (`Yes/No → 1/0`)  

🔗 **Dataset Link:**  
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

---

## 🔍 Exploratory Data Analysis (EDA)
The following analysis was performed:
- Checked for **missing values** and **duplicate records**
- Analyzed **attrition distribution**
- Studied relationships between attrition and:
  - Department  
  - Job Satisfaction  
  - Monthly Income  
- Created visualizations using **Matplotlib** and **Seaborn**

---

## 🧹 Data Preprocessing
Steps performed before training the model:
- Converted target variable (`Attrition`) into binary values
- Encoded categorical variables using **Label Encoding**
- Selected relevant features
- Split dataset into training and testing sets
- Applied **feature scaling** for consistency

---

## 🤖 Machine Learning Model
### ✅ Model Used: Random Forest Classifier

### ⭐ Reason for Selection
- Handles non-linear relationships effectively
- Reduces overfitting by combining multiple decision trees
- Provides **feature importance** for interpretability

---

## 📈 Model Evaluation
The model was evaluated using:
- Accuracy Score
- Confusion Matrix
- Classification Report

📌 **Accuracy Achieved:** ~85% to 88%  
*(May vary depending on random state and train-test split)*

---

## 🔑 Key Observations
- Employees with **low job satisfaction** show higher attrition rates
- **Monthly income** and **overtime** significantly impact attrition
- Random Forest identifies important features contributing to employee turnover

---

## 🚀 Suggestions for Improvement
To improve model performance further:
- Apply hyperparameter tuning using **GridSearchCV**
- Handle class imbalance using **SMOTE**
- Try advanced models like:
  - XGBoost
  - Gradient Boosting
  - Support Vector Machines (SVM)

---

## ⚙️ Steps to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VaidikaSharmaRCEW/EmployeeAttritionMachineLearning.git
