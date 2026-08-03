# 🎓 Student Placement Prediction

A Machine Learning project that predicts whether a student will be placed based on academic performance, technical skills, internships, communication skills, and other relevant attributes.

## 📌 Project Overview

This project uses supervised machine learning to classify whether a student will be placed or not. It includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, feature importance analysis, and prediction for new students.

---

## 🚀 Features

- Data preprocessing using Label Encoding
- Exploratory Data Analysis (EDA)
- Correlation Heatmap
- Placement distribution visualization
- CGPA and Coding Skills analysis
- Random Forest Classification
- Logistic Regression Classification
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - Classification Report
  - Confusion Matrix
- Feature Importance Visualization
- Prediction for a new student

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

---

## 📂 Dataset

The project uses separate training and testing datasets.

- `train.csv`
- `test.csv`

The target variable is:

- **Placement_Status**

---

## 📊 Exploratory Data Analysis

The notebook includes several visualizations to understand the dataset:

- Placement Status Distribution
- CGPA vs Placement Status
- Coding Skills vs Placement Status
- Feature Correlation Heatmap
- Feature Importance Chart

---

## 🤖 Machine Learning Models

### 1. Random Forest Classifier

- 300 Decision Trees
- Maximum Depth = 12
- Random State = 42

### 2. Logistic Regression

- Maximum Iterations = 1000
- Random State = 42

---

## 📈 Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 🔍 Feature Engineering

Categorical features are converted into numerical values using **Label Encoding**.

Encoded Features:

- Gender
- Degree
- Branch
- Placement Status (Target)

---

## 🎯 Prediction

The notebook also demonstrates how to predict the placement status of a new student using the trained Random Forest model.

---

## 📁 Project Structure

```
Student_Placement_Prediction/
│
├── project_placement_prediction.ipynb
├── train.csv
├── test.csv
├── README.md
```

---

## ▶️ How to Run

1. Clone this repository

```bash
git clone https://github.com/your-username/Student_placement_predictor.git
```

2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Open the notebook

```bash
jupyter notebook
```

or upload the notebook to Google Colab.

4. Run all cells sequentially.

---

## 📚 Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross Validation
- XGBoost and LightGBM models
- Model deployment using Streamlit or Flask
- Feature selection techniques
- Web application for real-time predictions

---

## 👨‍💻 Author

**Shanawas Hussain**

B.Tech in Artificial Intelligence

NIT Rourkela

GitHub: https://github.com/your-username
