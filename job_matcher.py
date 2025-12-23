import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# Get base directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

resume_path = os.path.join(BASE_DIR, "data", "resume.txt")
job_path = os.path.join(BASE_DIR, "data", "job.txt")


# -------------------------------
# Read files
# -------------------------------
with open(resume_path, "r", encoding="utf-8") as f:
    resume_text = f.read()

with open(job_path, "r", encoding="utf-8") as f:
    job_text = f.read()


# -------------------------------
# Simple text cleaning (NO NLTK)
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)  # remove symbols
    text = re.sub(r"\s+", " ", text)         # remove extra spaces
    return text.strip()


clean_resume = clean_text(resume_text)
clean_job = clean_text(job_text)


# -------------------------------
# Convert text to vectors
# -------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform([clean_resume, clean_job])


# -------------------------------
# Calculate similarity
# -------------------------------
similarity_score = cosine_similarity(vectors)[0][1]


# -------------------------------
# Output result
# -------------------------------
print("\nJob Matcher Result")
print("------------------")
print(f"Match Percentage: {similarity_score * 100:.2f}%\n")
