
from langchain.llms import OpenAI
from langchain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = "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"
# Function to load OpenAI model and get responses

def get_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),model_name = "davinci-002", temperature = 0.6)
    response = llm(question)
    return response


# Initialise streamlit app

st.set_page_config(page_title = "Q & A Demo")

st.header("Q & A Bot")

input = st.text_input("Input: ", key = "input")

response  = get_response(input)
submit = st.button("Submit")

if submit:
    st.subheader(" My answer :")
    st.write(response)