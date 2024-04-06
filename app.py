import streamlit as st
from transformers import pipeline

# Load Hugging Face model
model = pipeline("text-generation", model="gpt2")

# Streamlit app
st.title("Text Generation with GPT-2")

user_input = st.text_input("Enter text for completion:")
if user_input:
    # Generate text based on user input
    generated_text = model(user_input, max_length=80, do_sample=False)[0]['generated_text']
    st.write("Generated Text:")
    st.write(generated_text)
