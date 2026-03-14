# health-disease-prediction
Machine Learning based disease prediction web application using Flask
# Health Disease Prediction Web Application

## 📌 Project Overview

The **Health Disease Prediction System** is a machine learning based web application that predicts possible diseases based on user-selected symptoms.
The system uses a trained machine learning model and provides predictions through a simple web interface.

This project demonstrates the integration of **Machine Learning with Web Development**.

---

## 🚀 Features

* Predict diseases based on symptoms
* Simple and user-friendly web interface
* Machine learning model integration
* Real-time prediction results
* Lightweight and easy to run

---

## 🛠 Technologies Used

* Python
* Flask (Web Framework)
* Scikit-learn (Machine Learning Library)
* Pandas (Data Processing)
* HTML
* CSS

---

## 📂 Project Structure

health-disease-prediction

├── dataset
│ └── Testing.csv

├── model
│ └── train_model.py

├── templates
│ └── index.html

├── static
│ └── style.css

├── app.py
├── model.pkl
├── requirements.txt
└── README.md

---

## ⚙️ Installation and Setup

### Step 1: Clone the repository

git clone https://github.com/yourusername/health-disease-prediction.git

### Step 2: Navigate to the project folder

cd health-disease-prediction

### Step 3: Install required libraries

pip install -r requirements.txt

### Step 4: Train the model

python model/train_model.py

### Step 5: Run the application

python app.py

### Step 6: Open in browser

http://127.0.0.1:10000

---

## 🧠 Machine Learning Model

The project uses the **Decision Tree Classifier** algorithm to predict diseases based on symptoms.

Steps involved:

1. Load dataset
2. Train machine learning model
3. Save trained model as `model.pkl`
4. Integrate model with Flask web application

---

## 📊 Future Improvements

* Improve prediction accuracy with larger datasets
* Add more symptoms and diseases
* Implement deep learning models
* Add chatbot-based symptom interaction

---

## 👨‍💻 Author

Dharma Teja

---

## 📄 License

This project is for educational purposes.
