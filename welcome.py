import streamlit as st

def welcome_page():
    st.title("👨‍⚕️ Welcome to DocSpeak!")
    st.markdown("""
        Welcome to **DocSpeak**, your AI-powered health and wellness assistant.  
        Navigate using the sidebar to access features like PDF Chat, Health Trackers,  
        Chronic Conditions, and Pain Management Support.
    """)
    st.image("https://cdn.pixabay.com/photo/2017/02/01/22/02/doctor-2037601_1280.png", use_column_width=True)
