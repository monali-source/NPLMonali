import streamlit as st
import pandas as pd
import random

import base64  # Make sure this line is added to import the base64 module

def add_bg_from_local():
    # Use a raw string for the file path to avoid escape character issues
    with open(r"C:\Users\patel\Downloads\NLP\chatbot\img2.webp", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            color: white;  /* Font color */
        }}
        /* Customize button color */
        .stButton>button {{
            background-color: black !important;
            color: white !important;
        }}
        /* Customize text input font color */
        p {{
            color: white !important;
        }}
        h1 {{
        color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the background function
add_bg_from_local()




# Load the dataset
data = pd.read_csv('chatbot/Diseases_Symptoms.csv')

responses = {
    "What is your name?": "My name is Chatbot.",
    "How are you?": "I'm fine, thank you!",
    "What do you do?": "I'm a chatbot designed to help users.",
    "Hello": "Hello, how can i help you with  diseases, symptoms, or treatments!"
}

# Function to search for answers
def search_answer(question):
    result = data[data['Symptoms'].str.contains(question, case=False) | 
                  data['Treatments'].str.contains(question, case=False) |
                  data['Name'].str.contains(question, case=False)]
    
    
    return result

def get_response(question):
    # Convert the question to lowercase for case-insensitive comparison
    question_lower = question.lower()
    # Iterate over the responses dictionary and look for a matching key
    for key, value in responses.items():
        if question_lower == key.lower():
            return value
    # Return default response if no matching key is found
    return "I'm sorry, I don't understand that question."

# Streamlit UI
st.title("Medical FAQ Chatbot")

# Text input for user question
user_question = st.text_input("Ask me!")


# Button to search for answers
if st.button("Search"):
    if user_question:
        # Search for answers
        result = search_answer(user_question)
        # Display the result
        if not result.empty:
            st.write("Found matching diseases:")
            for index, row in result.iterrows():
                st.write(f"Disease: {row['Name']}")
                st.write(f"Symptoms: {row['Symptoms']}")
                st.write(f"Treatments: {row['Treatments']}")
                st.markdown("---")
        else:
                # If not found, get a response from predefined list
                st.write(get_response(user_question))