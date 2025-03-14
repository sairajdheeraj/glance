from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

API_KEY = os.getenv("GEMINI")
if not API_KEY:
    raise ValueError("API key is missing! Set GOOGLE_GENAI_API_KEY as an environment variable.")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-pro")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.json
        if "text" not in data or not data["text"].strip():
            return jsonify({"error": "Text input is required"}), 400

        response = model.generate_content(f"Summarize the following content in bullet points:\n\n{data['text']}")
        summary = response.text if response else "No summary generated."

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/explain", methods=["POST"])
def explain():
    try:
        data = request.json
        if "text" not in data or not data["text"].strip():
            return jsonify({"error": "Text input is required"}), 400

        response = model.generate_content(f"Explain the following content clearly and concisely:\n\n{data['text']}")
        explanation = response.text if response else "No explanation generated."

        return jsonify({"explanation": explanation})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
