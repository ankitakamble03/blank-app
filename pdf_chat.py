# pdf_chat.py
import streamlit as st
import openai

def ask_gpt(question, context, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a medical assistant."},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"}
        ]
    )
    return response['choices'][0]['message']['content']

def pdf_chat_page(api_key):
    st.header("📄 Chat with Medical PDF")
    uploaded_file = st.file_uploader("Upload a medical PDF", type=["pdf"])

    if uploaded_file:
        st.success("PDF uploaded. (Parsing logic would go here.)")
        # Placeholder text from parsed PDF
        text = "This is placeholder text extracted from the uploaded PDF."

        user_question = st.text_input("Ask a question about this document:")
        if user_question:
            try:
                answer = ask_gpt(user_question, text, api_key)
                st.markdown("**Answer:**")
                st.write(answer)
            except openai.error.AuthenticationError:
                st.error("Invalid API key. Please try again.")
            except openai.error.RateLimitError:
                st.error("You exceeded your current quota. Check your OpenAI billing.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
