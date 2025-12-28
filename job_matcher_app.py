import streamlit as st
import pandas as pd
from fpdf import FPDF

from job_matcher import get_top_n_jobs
#new one for the resume adding
# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Job Matcher Application",
    layout="wide"
)

st.title("Job Matcher Result")

# ------------------ SAMPLE JOB DATA ------------------
jobs = [
    {
        "title": "Python Developer",
        "company": "ABC Corp",
        "skills": {
            "python": 0.5,
            "sql": 0.3,
            "git": 0.2
        }
    },
    {
        "title": "Data Analyst",
        "company": "XYZ Ltd",
        "skills": {
            "excel": 0.4,
            "sql": 0.4,
            "python": 0.2
        }
    },
    {
        "title": "Backend Engineer",
        "company": "TechSoft",
        "skills": {
            "python": 0.6,
            "django": 0.3,
            "api": 0.1
        }
    }
]

# ------------------ RESUME UPLOAD ------------------
st.subheader("Upload Resume")
uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# ------------------ PROCESS AFTER UPLOAD ------------------
if uploaded_file is not None:

    # For now we simulate extracted skills
    candidate_skills = ["python", "sql", "excel"]

    # Get top job matches
    top_jobs = get_top_n_jobs(
        candidate_skills=candidate_skills,
        jobs=jobs,
        top_n=3
    )

    # Convert results to DataFrame
    df = pd.DataFrame(top_jobs)

    st.subheader("Top Job Matches")
    st.dataframe(df, use_container_width=True)

    # ------------------ CSV DOWNLOAD ------------------
    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="job_matches.csv",
        mime="text/csv"
    )

    # ------------------ PDF DOWNLOAD (FIXED) ------------------
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Top Job Matches", ln=True, align="C")
    pdf.ln(10)

    for _, row in df.iterrows():
        pdf.cell(
            200,
            10,
            f"{row['title']} at {row['company']} - Score: {row['score']}%",
            ln=True
        )

    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="job_matches.pdf",
        mime="application/pdf"
    )

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("Built with Streamlit | Job Matcher Project")
