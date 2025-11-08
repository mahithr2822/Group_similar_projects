import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        text = ""
    return text

def cluster_documents(doc_folder, n_clusters=2):
    docs, filenames = [], []

    for file in os.listdir(doc_folder):
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(os.path.join(doc_folder, file))
            if len(text.strip()) > 0:
                docs.append(text)
                filenames.append(file)

    if not docs:
        return {"error": "No valid PDF text found"}

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(docs)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)

    clusters = {}
    for i, label in enumerate(kmeans.labels_):
        clusters.setdefault(int(label), []).append(filenames[i])

    return clusters
