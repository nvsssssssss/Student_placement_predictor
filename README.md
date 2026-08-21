# Student Placement Prediction

A machine learning project that predicts whether a student is likely to be **Placed** or **Not Placed** based on academic performance, technical skills, internships, projects, aptitude scores, and other student attributes. Deployed as a live, interactive web app.

## Live Demo

🔗 **[Try the app here](https://student-placement-predictor-01.streamlit.app/)**

## Overview

The project uses a student placement dataset containing **45,000 training records** and multiple academic and skill-based features.

The workflow includes:

* Exploratory Data Analysis (EDA)
* Categorical feature encoding
* Random Forest classification
* Model evaluation
* Feature importance analysis
* Deployment as a live Streamlit web app for real-time predictions

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
* **Streamlit** — web app framework for deployment
* **Joblib** — model serialization

## Machine Learning Model

### Random Forest Classifier

The classification model is a Random Forest with:

* `n_estimators = 300`
* `max_depth = 12`
* `random_state = 42`

The model learns patterns from the student's academic and skill-related attributes to predict placement status.

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

The encoders fitted on the training data are also used to transform the test data and new student inputs consistently — saved as `encoders.pkl` and `target_encoder.pkl` for use at inference time.

## Model Evaluation

The model is evaluated using classification metrics including:

* Accuracy: **99.98%** 
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

A confusion matrix is also visualized to analyze correct and incorrect predictions.

## Feature Importance

The Random Forest model's feature importance scores are extracted to identify the features that contribute most to the model's predictions.

The project visualizes the **top 10 most important features**.

## Web App

A Streamlit web app (`app.py`) provides a real-time prediction interface:

* User fills in a form with the 13 student attributes (plus a placeholder Student ID)
* The app loads the saved model and encoders (`model.pkl`, `encoders.pkl`, `target_encoder.pkl`)
* Encodes the input consistently with training-time preprocessing
* Returns the predicted placement status with a confidence percentage

The app is deployed on **Streamlit Community Cloud**, connected directly to this GitHub repo for automatic redeployment on push.

## Project Structure

```text
Student_placement_predictor/
│
├── project_placement_prediction.ipynb   # Training notebook (EDA, encoding, training, evaluation)
├── app.py                               # Streamlit web app for live predictions
├── requirements.txt                     # Python dependencies
├── model.pkl                            # Trained Random Forest model
├── encoders.pkl                         # Fitted LabelEncoders for categorical features
├── target_encoder.pkl                   # Fitted LabelEncoder for the target variable
├── train.csv
├── test.csv
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/nvsssssssss/Student_placement_predictor.git
cd Student_placement_predictor
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the App Locally

```bash
streamlit run app.py
```

This opens the prediction form in your browser at `http://localhost:8501`.

## Running the Training Notebook

The model training workflow is implemented as a Jupyter/Google Colab notebook.

1. Open `project_placement_prediction.ipynb`.
2. Upload `train.csv` and `test.csv`.
3. Run the notebook cells sequentially.
4. The notebook performs EDA, preprocessing, model training, evaluation, feature analysis, and saves the model/encoder artifacts (`model.pkl`, `encoders.pkl`, `target_encoder.pkl`).

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
Random Forest Classifier
   ↓
Model Evaluation
   ↓
Feature Importance Analysis
   ↓
Model + Encoders Saved (joblib)
   ↓
Streamlit Web App
   ↓
Deployed on Streamlit Community Cloud
```

## Key Learning Outcomes

Through this project, the following concepts were applied:

* Classification with Random Forest
* Exploratory Data Analysis
* Categorical Feature Encoding
* Model Evaluation (Accuracy, Precision, Recall, F1-score)
* Confusion Matrix Analysis
* Feature Importance
* Model Serialization with Joblib
* Building an interactive web app with Streamlit
* End-to-end ML deployment (training → serialization → web interface → cloud hosting)

## Future Improvements

Potential improvements to the project include:

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Comparing additional classification algorithms
* Applying cross-validation
* Handling class imbalance if present
* Adding probability-based placement predictions with richer explanations (e.g. SHAP values)
* Improving preprocessing using pipelines and `ColumnTransformer`
* Dropping `Student_ID` as a training feature to eliminate ID-based leakage risk

## Disclaimer

This project is intended for educational and demonstration purposes. Placement predictions are based on the patterns present in the dataset and should not be treated as a definitive prediction of an individual's actual placement outcome.
