from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "message": "Haqdar Enterprise Backend is live and operational."
    })

@app.route("/api/match", methods=['GET'])
def match_opportunities():
    # Capture query parameters safely
    age = request.args.get("age", "0")
    income = request.args.get("income", "0")
    state = request.args.get("state", "All India")
    category = request.args.get("category", "General")

    # Hardcoded deterministic dataset for verification
    mock_database = [
        {
            "id": "mah-001",
            "title": "Post-Matric Scholarship Scheme for SC Students",
            "domicile": "Maharashtra",
            "type": "Scholarship",
            "official_link": "https://mahadbtmahadbt.gov.in/"
        }
    ]

    return jsonify({
        "success": True,
        "count": len(mock_database),
        "matches": mock_database,
        "received_params": {
            "age": age,
            "income": income,
            "state": state,
            "category": category
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
