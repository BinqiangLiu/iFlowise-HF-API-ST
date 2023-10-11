import streamlit as st
import requests

API_URL = "https://binqiangliu-iflowiseai.hf.space/api/v1/prediction/d3912c84-735c-4c64-99c3-acc60cad59f0"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
  
user_question=st.text_input("Enter your question:")
if user_question !="" and not user_question.strip().isspace() and not user_question == "" and not user_question.strip() == "" and not user_question.isspace():
  with st.spinner("AI Thinking...Please wait a while to Cheers!"):
      question_prefix+"Assistant is designed to answer user questions only based on information from USinoIP's website www.usinoip.com. If Assistant is not able to find an answer to user question, just response to the user that assistant cannot find an answer. Assistant should never make up an answer. Remember, Assistant should ONLY use information from USinoIP's website www.usinoip.com as the knowledge base."
      input_question=question_prefix+user_question
      output = query({
      "question": input_question,
    })
    st.write("AI Response:")
    st.write(output)
