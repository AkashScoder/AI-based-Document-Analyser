import openai
import PyPDF2
import streamlit as st
import spacy
from twilio.rest import Client
import re
import os  # For loading environment variables

nlp = spacy.load("en_core_web_sm")

# Load sensitive keys from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')  # Set this in your environment
account_sid = os.getenv('TWILIO_ACCOUNT_SID')  # Set this in your environment
auth_token = os.getenv('TWILIO_AUTH_TOKEN')    # Set this in your environment
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')  # Set this in your environment

def add_custom_css():
    st.markdown(
        """
        <style>
        /* Add a background gradient and modify the font */
        body {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        
        /* Style headers */
        h1, h2, h3 {
            color: #4c72b0;
            font-weight: bold;
        }

        /* Customize the input and text area */
        input, textarea {
            background-color: #ffffff !important;
            color: #000000 !important;  /* Text color black on white background */
            border-radius: 8px;
            border: 1px solid #cccccc;
            padding: 10px;
            margin-bottom: 10px;
        }

        /* Style the file uploader */
        .stFileUploader {
            border: 2px solid #4c72b0;
            border-radius: 10px;
            padding: 10px;
        }

        /* Customize button appearance */
        .stButton button {
            background-color: #4c72b0 !important;
            color: white !important;
            border-radius: 10px !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
        }

        /* Style success and error messages */
        .stAlert {
            border-radius: 10px;
            padding: 20px;
            background-color: #d3e9f5;
            border-left: 5px solid #4c72b0;
            color: #000000 !important;  /* Text color black */
        }

        .stTextArea textarea {
            background-color: #ffffff !important;  /* White background */
            color: #000000 !important;  /* Black text */
            border: 1px solid #cccccc;
            border-radius: 10px;
        }

        /* Add custom margins and padding */
        .stApp {
            padding-top: 50px;
            padding-bottom: 50px;
            padding-left: 20px;
            padding-right: 20px;
        }

        /* Style the scrollable document text area */
        .scrollable-document {
            max-height: 300px;
            overflow-y: scroll;
            background-color: #ffffff; /* White background */
            color: #000000 !important;  /* Black text */
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #cccccc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# The rest of your document extraction and analysis code here...

if __name__ == "__main__":
    # Run the Streamlit app
    document_analyzer_app()
