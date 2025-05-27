# navigation.py
import streamlit as st
from welcome import welcome_page
from pdf_chat import pdf_chat_page
from tracker import tracker_page
from chronic_conditions import chronic_conditions_page
from pain_management import pain_management_page

def main_navigation(api_key):
    st.sidebar.title("🩺 MediSpeak Navigation")
    page = st.sidebar.radio("Go to", [
        "Welcome", "📄 PDF Chat", "📊 Health Tracker", "🧬 Chronic Conditions", "🤕 Pain Management"
    ])

    if page == "Welcome":
        welcome_page()
    elif page == "📄 PDF Chat":
        pdf_chat_page(api_key)
    elif page == "📊 Health Tracker":
        tracker_page()
    elif page == "🧬 Chronic Conditions":
        chronic_conditions_page()
    elif page == "🤕 Pain Management":
        pain_management_page()
