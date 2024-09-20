import streamlit as st

text_answer = st.text_input("Write something here:")

st.download_button("Download some text", text_answer)