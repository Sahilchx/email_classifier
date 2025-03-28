import streamlit as st
import pickle
import re
# Streamlit UI for Email Classification
st.title("Email Spam Classifier")

# Remove special characters, numbers, and extra spaces(clean function)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Load saved model and vectorizer
def load_model():
    with open("random_forest.pkl", "rb") as rf_file:
        loaded_model = pickle.load(rf_file)
    with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
        loaded_vectorizer = pickle.load(vectorizer_file)
    return loaded_model, loaded_vectorizer

model, vectorizer = load_model()

# User input
user_input = st.text_area("Enter the email content:")
if st.button("Classify"):
    if user_input:
        user_input_cleaned = clean_text(user_input)#text goes for cleaning
        user_input_tfidf = vectorizer.transform([user_input_cleaned])#after cleaning text numeric vector is created by tfid vectorizer
        prediction = model.predict(user_input_tfidf)#prediction is done by model
        result = "Spam" if prediction[0] == 1 else "Ham"
        st.write(f"### Prediction: {result}")
    else:
        st.warning("Please enter an email to classify.")
