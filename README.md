# 📧 Email Classifier using Machine Learning  

This project is an **email classification system** that detects **spam or ham (legitimate emails)** using **Machine Learning models**. It utilizes feature extraction techniques like **TF-IDF vectorization** and models such as **Naïve Bayes, Decision Tree, and Random Forest**.

---

## 🚀 Features  
✅ Classifies emails as **spam** or **not spam**  
✅ Uses **TF-IDF** for feature extraction  
✅ Implements **Naïve Bayes, Decision Tree, and Random Forest** models  
✅ Supports **real-time classification**  
✅ Trained on a large email dataset  

---
## 🛠️ Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/Sahilchx/email_classifier.git
cd email_classifier
```
### 2️⃣ Install Required Libraries
Make sure you have Python 3.7+ installed. Install dependencies using:
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the Classifier
```sh
python main.py
```
---
## 📂 Project Structure
```sh
📦 email_classifier
│-- 📜 email.ipynb               # Jupyter Notebook for experiments
│-- 📜 main.py                   # Main script for classification
│-- 📂 models
│   ├── decision_tree.pkl        # Trained Decision Tree model
│   ├── naive_bayes.pkl          # Trained Naïve Bayes model
│   ├── random_forest.pkl        # Trained Random Forest model
│-- 📂 data
│   ├── spam_Emails_data.csv     # Dataset used for training
│   ├── tfidf_vectorizer.pkl     # TF-IDF Vectorizer
│-- 📜 requirements.txt           # Required libraries
│-- 📜 README.md                  # Project documentation

```
---
## 🧠 How It Works

### 1️⃣ Preprocessing
The dataset is cleaned by removing stopwords, punctuation, and unnecessary characters
### 2️⃣ Feature Extraction
Converts email text into numerical format using TF-IDF vectorization
### 3️⃣ Model Training
Trains models (Naïve Bayes, Decision Tree, Random Forest) on labeled data
### 4️⃣ Prediction
Given a new email, the model predicts if it's spam or not spam

---
## 📊 Machine Learning Models Used

✔ **Naïve Bayes Classifier**  
✔ **Decision Tree Classifier**  
✔ **Random Forest Classifier**  

---
## 📂 Dataset  
You can download the dataset from [this link](https://www.kaggle.com/datasets/meruvulikith/190k-spam-ham-email-dataset-for-classification).

---
## 💡 Interesting Findings

- 🟠 **Naïve Bayes** performed well but mistakenly classified simple ham emails as spam.  
- 🔵 **Decision Tree** reached **96.8% accuracy**.  
- 🟢 **Random Forest** outperformed with **98.6% accuracy** & better real-time predictions.  

---
## 🔮 Future Work

- ⚡ Use **Deep Learning** and **NLP models** for better classification.  
- 📈 Use **real-time datasets** to improve optimal and more accurate predictions.  
---
