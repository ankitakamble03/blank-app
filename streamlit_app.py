# app2.py
import streamlit as st
from navigation import main_navigation

st.set_page_config(page_title="MediSpeak", layout="wide")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    try:
        main_navigation(api_key)
    except Exception as e:
        st.sidebar.error(f"Error: {e}")
else:
    st.sidebar.warning("Please enter your OpenAI API key to continue.")
    st.info("You can get your API key from https://platform.openai.com/account/api-keys")
