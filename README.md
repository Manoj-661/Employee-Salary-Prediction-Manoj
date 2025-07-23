# 💼 Salary Prediction using Machine Learning

This project predicts whether an individual earns **more than 50K USD annually** based on personal and work-related attributes using various machine learning models. A final **Streamlit web app** is built for real-time prediction.

---

## 📌 Project Overview

- **Dataset:** UCI Adult Income Dataset
- **Goal:** Predict salary category (`<=50K` or `>50K`)
- **ML Models Used:**
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Random Forest Classifier ✅ *(Final model)*
  - Artificial Neural Network (ANN)

---

## 🚀 Web App Demo

The web app is built using **Streamlit**. It lets users input details like age, education, work class, etc., and predicts the salary category.

### ▶️ How to Run:

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/salary-prediction-app.git
   cd salary-prediction-app
2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:

   streamlit run salary_prediction_app.py


  | File                       | Description                          |
| -------------------------- | ------------------------------------ |
| `salary_prediction_app.py` | Streamlit app file                   |
| `final_salary_model.pkl`   | Trained RandomForest model           |
| `model_columns.pkl`        | Feature columns used during training |
| `README.md`                | Project documentation                |
| `requirements.txt`         | Python dependencies                  |



| Model               | Accuracy (%) |
| ------------------- | ------------ |
| Logistic Regression | 81.98        |
| KNN                 | 82.96        |
| SVM                 | 83.40        |
| ANN (MLP)           | 84.20        |
| ✅ Random Forest     | **84.75**    |



📈 Features Used
Age

Workclass

Education

Marital Status

Occupation

Relationship

Race

Gender

Capital Gain / Loss

Hours per Week

Native Country


✅ Conclusion
Random Forest gave the best performance among the tested models and was deployed in the final Streamlit web app. This project demonstrates the end-to-end pipeline from data cleaning and feature engineering to model evaluation and deployment.
