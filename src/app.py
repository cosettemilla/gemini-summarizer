from flask import Flask, request, jsonify
from src.gemini_client import summarize_with_gemini

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    summary = summarize_with_gemini(text)
    return jsonify({"summary": summary})
