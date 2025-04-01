from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/upload', methods=['POST'])
def analyze_resume():
    try:
        data = request.json
        resume_text = data.get("resume_text", "")

        # Replace with actual fraud detection logic
        fraud_probability = 0.20139022204298757 if resume_text else None
        classification = "Genuine Resume ✅" if fraud_probability is not None and fraud_probability < 0.5 else "Fraudulent Resume ❌"

        response_data = {
            "final_classification": classification,
            "fraud_probability": fraud_probability if fraud_probability is not None else 0.0  # Ensure it's always a number
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
