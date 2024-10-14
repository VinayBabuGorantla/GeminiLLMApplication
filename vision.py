from dotenv import load_dotenv
load_dotenv() # Load all the environment variables

import streamlit as st
import os
from PIL import Image

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUnction to load Gemini and Gemini pro model and get responses

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


# Initialize streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input Prompt: ",key="input")
upload_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
submit=st.button("Tell me about the image")

# When submit is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)