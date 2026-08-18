from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#TF(term frequency): how often this word appears in the doc. 
#IDF(inverse document frequency): how rare a word is across all documents being compared
#tf-idf is TF X IDF

def calculate_match_score(resume_text , jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text , jd_text])

    similarity = cosine_similarity(vectors[0:1] , vectors[1:2])

    score = round(similarity[0][0] * 100 , 2)
    return score   
