# 📘 Document Clustering Project

This project automatically groups similar PDF documents using **machine learning**.  
It provides a simple web interface for uploading files and viewing clustered results.

---

## 🧩 Project Overview

The system has two parts:
- **Backend:** Flask-based API that handles file uploads and document clustering.  
- **Frontend:** Simple HTML + JavaScript page to upload and view clusters.

Documents are clustered based on text similarity using **TF-IDF** and **K-Means**.

---

Here is your complete, production-ready README.md —
a single document containing project overview, setup, backend, frontend, clustering code, usage, and troubleshooting.
Copy this as-is into your project root:

# 📘 DOCUMENT CLUSTERING PROJECT

Automatically group similar PDF documents using **Machine Learning** and a simple **Flask + HTML interface**.

---

## 🧠 OVERVIEW

This project detects similarity among documents and groups them using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **K-Means clustering**.  
It extracts text from uploaded PDFs, vectorizes the content, and forms clusters based on textual similarity.  

Users can:
- Upload multiple PDF documents.
- Run document clustering.
- Get cluster results in JSON format.

---

## 🧩 SYSTEM ARCHITECTURE



Frontend (HTML + JS) ──► Flask Backend ──► Clustering Model (TF-IDF + KMeans)
▲ │
└────── JSON Results ◄──┘


---

## ⚙️ TECHNOLOGY STACK

| Layer | Tools |
|-------|-------|
| Language | Python, JavaScript |
| Backend | Flask |
| Frontend | HTML, CSS |
| Machine Learning | scikit-learn |
| PDF Text Extraction | PyPDF2 |

---

## 🏗️ PROJECT STRUCTURE



Group_simi_docs/
│
├── backend/
│ ├── app.py # Flask backend
│ ├── clustering.py # ML clustering logic
│ ├── requirements.txt # Python dependencies
│ ├── uploads/ # Uploaded PDFs
│ └── sample_docs/ # Example input PDFs
│
└── frontend/
├── index.html # Web UI
├── script.js # JS logic
└── style.css # Stylesheet


---

## 🧰 REQUIREMENTS

- Python 3.9 or above  
- pip package manager  
- Google Chrome or any modern browser  

Install dependencies from `backend/requirements.txt`:



Flask==3.0.3
Flask-Cors==4.0.0
scikit-learn==1.5.0
numpy==1.26.4
pandas==2.2.2
PyPDF2==3.0.1


---

## ⚙️ SETUP AND EXECUTION

### 1️⃣ Create Virtual Environment
```bash
python3 -m venv venv

2️⃣ Activate Virtual Environment

macOS / Linux

source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install Dependencies
cd backend
pip install -r requirements.txt

4️⃣ Start Flask Server
python3 app.py


Expected output:

* Running on http://127.0.0.1:5000

5️⃣ Launch Frontend

Open the file manually in browser:

frontend/index.html


You will see:

File picker

“Upload” and “Get Clusters” buttons
