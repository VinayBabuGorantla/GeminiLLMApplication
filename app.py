from dotenv import load_dotenv
load_dotenv() # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUnction to load Gemini and Gemini pro model and get responses

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# Initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.write(response)



