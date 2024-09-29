import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDKJAjHWkHgELtF7eXOga5n2jIWfbgL6zA")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response = model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("file not uploaded")
    
st.set_page_config(page_title="GenAI Future Scan")
st.sidebar.header("SmartScan AI Bot")
st.sidebar.write("This AI Bot prioritizes User-Centric Design, ensuring intuitive navigation while delivering Real-Time Insights to empower users in making informed decisions.")
st.sidebar.write("Powered by Google Gemini AI")
st.sidebar.write("Made by Nidhurshek")
st.header("SmartScan AI Bot")
st.subheader("Made by Nidhurshek")
st.subheader("Ask anything to SmartScan AI Bot")
input = st.text_input("What do you want the AI to do ?",key="input")
uploaded_file = st.file_uploader("Choose an Image",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit = st.button("Lets Go")

input_prompt = """
You are an expert in reading images. We are going to upload an image and you will have to
answer any type of questions asked by the user. Always greet the user first. Always keep fonts uniform
At the end,make sure to repeat the name of our app "SmartScan BillBot" ans ask user to use it again. Provide accurate information
to the user. Dynamically change colours to attract users.
"""



if ssubmit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know:")
    st.write(response)
