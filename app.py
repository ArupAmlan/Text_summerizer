import streamlit as st
from transformers import pipeline

def load_model():
    return pipeline("summarization", model = "facebook/bart-large-cnn")

summarizer = load_model()


st.title("Text Summarizer App")
st.markdown("Enter long paragraph and get a short summary of it")

text_input = st.text_area("Paste your text here:", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text_input, max_length=100, min_length=30, do_sample=False)
            st.success("Done!")
            st.subheader("🔍 Summary:")
            st.write(summary[0]['summary_text'])