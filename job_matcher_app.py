import os
import re
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Text cleaning function
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# -----------------------------
# Streamlit interface
# -----------------------------
st.title("Job Matcher Project")
st.write("Compare your resume with a job description and get match %")

resume_text = st.text_area("Paste Resume Text Here")
job_text = st.text_area("Paste Job Description Here")

if st.button("Check Match"):
    if resume_text.strip() == "" or job_text.strip() == "":
        st.warning("Please enter both resume and job description!")
    else:
        clean_resume = clean_text(resume_text)
        clean_job = clean_text(job_text)

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([clean_resume, clean_job])
        similarity_score = cosine_similarity(vectors)[0][1]

        st.success(f"Match Percentage: {similarity_score * 100:.2f}%")
