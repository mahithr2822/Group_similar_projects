from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from clustering import cluster_documents  # make sure clustering.py exists

# Folder setup
UPLOAD_FOLDER = "backend/uploads"
DOC_FOLDER = "backend/sample_docs"

app = Flask(__name__)
CORS(app)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Root route (fix for 404) ---
@app.route("/", methods=["GET"])
def home():
    return "✅ Flask backend is running. Use /upload to upload files or /cluster to group them."

# --- Upload route ---
@app.route("/upload", methods=["POST"])
def upload_files():
    files = request.files.getlist("files")
    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    uploaded = 0
    for file in files:
        if file.filename.endswith(".pdf"):
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            uploaded += 1

    return jsonify({"message": f"{uploaded} PDF files uploaded successfully"})

# --- Clustering route ---
@app.route("/cluster", methods=["GET"])
def cluster_docs():
    clusters = cluster_documents(UPLOAD_FOLDER)
    return jsonify(clusters)

# --- Run server ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
