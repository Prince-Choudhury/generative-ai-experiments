import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the Streamlit page
st.header('Research Tool 🚀')

# Get user input
user_input = st.text_input('Enter your prompt')

# Initialize the Gemini model
# Make sure to set your GOOGLE_API_KEY in your .env file
# Example: GOOGLE_API_KEY="Your_API_Key_Here"
try:
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
except Exception as e:
    st.error(f"Error initializing the model: {e}")
    st.info("Please ensure your GOOGLE_API_KEY is set correctly in a .env file.")
    model = None

# Create a button to trigger the summarization
if st.button('Summarize'):
    if model and user_input:
        with st.spinner('Gemini is thinking...'):
            try:
                # Invoke the model with the user's input
                result = model.invoke(user_input)
                # Display the result
                st.write(result.content)
            except Exception as e:
                st.error(f"An error occurred while processing your request: {e}")
    elif not user_input:
        st.warning("Please enter a prompt.")