from flask import Flask, request, jsonify
from src.gemini_client import summarize_with_gemini
from flask import render_template, request

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

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/web-summarize", methods=["POST"])
def web_summarize():
    text = request.form.get("text", "")
    from gemini_client import summarize_with_gemini
    summary = summarize_with_gemini(text)
    return render_template("index.html", summary=summary)
from flask import Flask, request, jsonify, render_template
from src.gemini_client import summarize_with_gemini

app = Flask(__name__)


# ---------------------------
# Health Check
# ---------------------------
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# ---------------------------
# Homepage (Web UI)
# ---------------------------
@app.route("/")
def homepage():
    return render_template("index.html")


# ---------------------------
# Web Form → Summarize
# ---------------------------
@app.route("/web-summarize", methods=["POST"])
def web_summarize():
    text = request.form.get("text", "")
    if not text.strip():
        return render_template("index.html", summary="Error: No text provided.")

    try:
        summary = summarize_with_gemini(text)
        return render_template("index.html", summary=summary)
    except Exception as e:
        return render_template("index.html", summary=f"Error: {str(e)}")


# ---------------------------
# API Endpoint (JSON)
# ---------------------------
@app.route("/summarize", methods=["POST"])
def summarize_api():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    summary = summarize_with_gemini(text)
    return jsonify({"summary": summary})


# ---------------------------
# Run (local dev only)
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
