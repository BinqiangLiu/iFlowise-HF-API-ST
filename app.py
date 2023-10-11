import streamlit as st
import requests

API_URL = "https://binqiangliu-iflowiseai.hf.space/api/v1/prediction/d3912c84-735c-4c64-99c3-acc60cad59f0"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
  
user_question=st.text_input("Enter your question:")
if user_question !="" and not user_question.strip().isspace() and not user_question == "" and not user_question.strip() == "" and not user_question.isspace():
  with st.spinner("AI Thinking...Please wait a while to Cheers!"):
    output = query({
      "question": user_question,
    })
    st.write("AI Response:")
    st.write(output)
