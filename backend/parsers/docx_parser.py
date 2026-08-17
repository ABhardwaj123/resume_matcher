from docx import Document

def extract_text_from_docs(file):
    doc = Document(file)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text

