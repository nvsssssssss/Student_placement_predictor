# Student Placement Prediction

A machine learning project that predicts whether a student is likely to be **Placed** or **Not Placed** based on academic performance, technical skills, internships, projects, aptitude scores, and other student attributes.

## Overview

The project uses a student placement dataset containing **45,000 training records** and multiple academic and skill-based features.

The workflow includes:

* Exploratory Data Analysis (EDA)
* Categorical feature encoding
* Random Forest classification
* Logistic Regression classification
* Model evaluation
* Feature importance analysis
* Prediction on new student profiles

## Dataset

The dataset contains the following features:

| Feature                | Description                          |
| ---------------------- | ------------------------------------ |
| `Student_ID`           | Unique student identifier            |
| `Age`                  | Student age                          |
| `Gender`               | Student gender                       |
| `Degree`               | Degree type                          |
| `Branch`               | Academic branch                      |
| `CGPA`                 | Cumulative GPA                       |
| `Internships`          | Number of internships                |
| `Projects`             | Number of projects                   |
| `Coding_Skills`        | Coding skill rating                  |
| `Communication_Skills` | Communication skill rating           |
| `Aptitude_Test_Score`  | Aptitude test score                  |
| `Soft_Skills_Rating`   | Soft skills rating                   |
| `Certifications`       | Number of certifications             |
| `Backlogs`             | Number of academic backlogs          |
| `Placement_Status`     | Target variable: Placed / Not Placed |

## Technologies Used

* **Python**
* **Pandas** — data manipulation
* **NumPy** — numerical operations
* **Matplotlib** — visualization
* **Seaborn** — exploratory data analysis
* **Scikit-learn** — machine learning and evaluation

## Machine Learning Models

### 1. Random Forest Classifier

The primary classification model is a Random Forest with:

* `n_estimators = 300`
* `max_depth = 12`
* `random_state = 42`

The model learns patterns from the student's academic and skill-related attributes to predict placement status.

### 2. Logistic Regression

Logistic Regression is also trained as a second classification model for comparison.

## Exploratory Data Analysis

The project performs several analyses to understand relationships between student characteristics and placement outcomes.

### Placement Distribution

Analyzes the distribution of students across the `Placed` and `Not Placed` categories.

### CGPA vs Placement

A box plot is used to examine the relationship between CGPA and placement status.

### Coding Skills vs Placement

A violin plot is used to visualize the distribution of coding skill ratings across placement outcomes.

### Correlation Analysis

A correlation heatmap is used to examine relationships between numerical features and identify features associated with placement status.

## Feature Encoding

Categorical variables are converted into numerical representations using **LabelEncoder**.

The following features are encoded:

* Gender
* Degree
* Branch
* Placement Status

The encoders fitted on the training data are also used to transform the test data and new student inputs consistently.

## Model Evaluation

The models are evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

A confusion matrix is also visualized to analyze correct and incorrect predictions.

## Feature Importance

The Random Forest model's feature importance scores are extracted to identify the features that contribute most to the model's predictions.

The project visualizes the **top 10 most important features**.

## Making a Prediction

The notebook includes an example of predicting the placement outcome of a new student.

Example input:

```python
new_student = pd.DataFrame([{
    "Student_ID": 99999,
    "Age": 22,
    "Gender": ...,
    "Degree": ...,
    "Branch": ...,
    "CGPA": 8.5,
    "Internships": 2,
    "Projects": 4,
    "Coding_Skills": 8,
    "Communication_Skills": 7,
    "Aptitude_Test_Score": 80,
    "Soft_Skills_Rating": 7,
    "Certifications": 2,
    "Backlogs": 0
}])

pred = rf.predict(new_student)

print(
    "Placement Prediction:",
    target_encoder.inverse_transform(pred)[0]
)
```

The model returns either:

```text
Placed
```

or

```text
Not Placed
```

## Project Structure

```text
student-placement-prediction/
│
├── project_placement_prediction.ipynb
├── train.csv
├── test.csv
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd student-placement-prediction
```

Install the required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Running the Project

The project is implemented as a Jupyter/Google Colab notebook.

1. Open `project_placement_prediction.ipynb`.
2. Upload `train.csv` and `test.csv`.
3. Run the notebook cells sequentially.
4. The notebook performs EDA, preprocessing, model training, evaluation, feature analysis, and prediction.

## Workflow

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Categorical Feature Encoding
   ↓
Train/Test Data Preparation
   ↓
Random Forest + Logistic Regression
   ↓
Model Evaluation
   ↓
Feature Importance Analysis
   ↓
New Student Placement Prediction
```

## Key Learning Outcomes

Through this project, the following machine learning concepts were applied:

* Classification
* Exploratory Data Analysis
* Categorical Feature Encoding
* Random Forest
* Logistic Regression
* Model Evaluation
* Confusion Matrix
* Precision, Recall and F1-score
* Feature Importance
* Prediction on unseen data

## Future Improvements

Potential improvements to the project include:

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Comparing additional classification algorithms
* Applying cross-validation
* Handling class imbalance if present
* Building a web interface for real-time predictions
* Deploying the trained model as an API
* Adding probability-based placement predictions
* Improving preprocessing using pipelines and `ColumnTransformer`

## Disclaimer

This project is intended for educational and demonstration purposes. Placement predictions are based on the patterns present in the dataset and should not be treated as a definitive prediction of an individual's actual placement outcome.
