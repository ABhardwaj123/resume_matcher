import re

def extract_skills(text , skills_list):

    lc_text = text.lower()
    matching_skills = []

    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, lc_text):
            matching_skills.append(skill)

    return matching_skills

