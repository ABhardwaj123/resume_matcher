from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile , Form
from parsers.pdf_parser import extract_text_from_pdf
from parsers.docx_parser import extract_text_from_docs
from matching.tfidf_matcher import calculate_match_score
from matching.skills_extractor import extract_skills
import json


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


with open("data/skills_list.json" , "r") as f:
    skills_list = json.load(f)


@app.get('/')
def home():
    return {"status": "ok123"}


@app.post('/match')
def upload(resume: UploadFile, jd_text: str = Form(...)):

    extracted_text = ""

    if resume.filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(resume.file)
    elif resume.filename.endswith(".docx"):
        extracted_text = extract_text_from_docs(resume.file)
    else:
        return {"error": "invalid resume format"}

    score = calculate_match_score(extracted_text, jd_text)

    resume_skills = extract_skills(extracted_text , skills_list)
    jd_skills = extract_skills(jd_text , skills_list)

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = resume_set & jd_set
    missing_skills = jd_set - resume_set


    return {
        "score": score,
        "matchedSkills": list(matched_skills),
        "missingSkills": list(missing_skills)
    }