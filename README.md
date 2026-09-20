# 🎓 Student Marks Prediction

A Machine Learning project that predicts a student's final marks based on:

* Study Hours
* Attendance
* Previous Marks

This project uses **Multiple Linear Regression** to make predictions.

The trained model is deployed using **Streamlit** to provide a simple web application for making predictions.
## 🚀 Features

* Predicts a student's final marks
* Uses Study Hours, Attendance, and Previous Marks as input
* Uses Multiple Linear Regression
* Provides predictions through a Streamlit web app
* Displays model performance using MAE and R² Score
## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub
## 📊 Dataset

The dataset contains 100 student records.

### Input Features

* **Study Hours** — Number of hours a student studies
* **Attendance** — Student attendance percentage
* **Previous Marks** — Student's previous marks

### Target

* **Final Marks** — The final marks predicted by the machine learning model
## 🤖 Machine Learning Model

This project uses **Multiple Linear Regression** to predict final marks.

The model learns the relationship between the input features and final marks:

**Final Marks = w₁(Study Hours) + w₂(Attendance) + w₃(Previous Marks) + b**

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The model is trained using the training data and evaluated on unseen testing data.
## 📈 Model Performance

The model was evaluated on 20 unseen test samples.

* **Mean Absolute Error (MAE):** 3.81 marks
* **R² Score:** 0.7792

The MAE indicates that the model's predictions differ from the actual marks by about 3.81 marks on average.

The R² Score indicates that the model explains approximately 77.9% of the variation in the target values for this test set.
## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/hassankhankhail48-droid/student-marks-prediction.git
```

### 2. Open the project folder

```bash
cd student-marks-prediction
```

### 3. Install the required libraries

```bash
pip install numpy pandas scikit-learn joblib streamlit
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.
## 📁 Project Structure

```text
student-marks-prediction/
│
├── app.py
├── student_marks_model.pkl
└── README.md
```

### File Description

* `app.py` — Streamlit web application
* `student_marks_model.pkl` — Trained Linear Regression model
* `README.md` — Project documentation
