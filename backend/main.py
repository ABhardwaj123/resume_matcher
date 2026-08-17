from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile , Form

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def home():
    return {"status": "ok123"}


@app.post('/match')
def upload(resume: UploadFile, jd_text: str = Form(...)):
    print(resume.filename)
    print(len(jd_text))

    return {
        "score": 72,
        "matchedSkills": ["python", "sql"],
        "missingSkills": ["docker", "kubernetes"]
    }